import typing

import mercadopago
from bson import ObjectId
from dateutil.relativedelta import *

from .dates import (calculate_payment_date, get_periodo, set_next_vigency,
                    today_argentina)
from .format import datetime_parser
from .init_creds import init_mongo

db = init_mongo()


def member_unsubscribe(member: dict, reason, source, unsubscribe_request=False, status_boleta_inactivado='expired'):
    """ Da de baja un socio modificando los parámetros necesarios
       :param member: objeto de cliente a dar de baja
       :type receiver: dict
       :param reason: motivo de la baja
       :type template: str
       :param unsubscribe_request: es True si el cliente es 'baja' y puede seguir ingresando
       :type unsubscribe_request: bool, optional
       :return: None
       :rtype: None
       """

    status = 'baja' if unsubscribe_request else 'inactivo'

    history_event = create_history_event(member, status, source, reason)

    db.clientes.update_one(
        {"_id": member["_id"]},
        {
            "$push": {
                "history2": history_event
            },
            "$set": {
                "next_payment_date": None,
                "status": status
            }
        }
    )

    db.boletas.update_many(
        {
            "member_id": member["_id"],
            "status": {
                "$in": ["error", "rejected", "pending_efectivo"]
            }
        },
        {
            "$set": {
                "status": status_boleta_inactivado
            }
        }
    )


def create_history_event(member, event_type, source, reason=None):

    if event_type == 'inactivo':
        event_type = 'inactivacion'

    history_event = {
        'event': event_type,
        'date_created': today_argentina(),
        'source': source
    }
    if reason:
        history_event["reason"] = reason

    if event_type in ['alta', 'baja', 'inactivacion', 'revertir_baja']:
        history_event['plan'] = member["active_plan_id"]

        if 'discounts' in member and member["discounts"] and len(member["discounts"]) > 0:
            history_event['discounts'] = member['discounts']

    elif event_type == "cambio_tarjeta":
        history_event["card_id"] = member["active_card"]

    return history_event


def restore_client_from_payment(payment_id: int, sdk: mercadopago.SDK) -> typing.Union[dict, None]:
    """ Método que crea la estructura de un cliente nuevo a partir de un pago de mercadopago.

    :param payment_id: id del pago a analizar
    :type payment_id: int
    :param sdk: sdk de mercadopago para el cual se creo el pago
    :type sdk: mercadopago.SDK
    :return: diccionario de cliente
    :rtype: dict
    """
    payment_response = sdk.payment().get(payment_id)

    if payment_response['status'] >= 400:
        return

    payment = datetime_parser(payment_response['response'])

    try:
        email = payment['additional_info']['items'][0]['description'].split(
            '-')[2].strip().lower()
    except:
        return

    plan = ObjectId(payment['additional_info']['items'][0]['id'])
    nombre = payment['additional_info']['payer']['first_name']
    apellido = payment['additional_info']['payer']['last_name']
    celular = payment['additional_info']['payer']['phone']['number']

    calle = payment['additional_info']['shipments']['receiver_address']['street_name']
    altura = int(payment['additional_info']['shipments']
                 ['receiver_address']['street_number'])
    localidad = payment['additional_info']['shipments']['receiver_address']['city_name']
    provincia = payment['additional_info']['shipments']['receiver_address']['state_name']

    documento = payment['point_of_interaction']['transaction_data']['subscription_id'].split(
        '-')[-1]

    today = today_argentina()
    f_vigencia_apto = today + relativedelta(days=30)

    socio = {
        'nombre': nombre,
        'apellido': apellido,
        'celular': celular,
        'email': email,
        'documento': documento,
        'domicilio': {
            'calle': calle,
            'altura': str(altura),
            'apto_lote': 'n/a',
            'localidad': localidad,
            'provincia': provincia,
            'código postal': '1000'
        },
        'status': 'activo',
        'payment_ids': [payment['id']],
        'last_payment_id': payment['id'],
        'active_plan_id': plan,
        'cobros_recurrentes': 0,
        'nacimiento': '22/02/2022',
        'preferred_payment_method': 'tarjeta',
        'brand_name': 'SportClub',
        'discounts': [],
        'cards': [],
        'apto_medico': {
            'url': '',
            'status': 'pendiente',
            'fecha_vigencia': f_vigencia_apto.replace(day=f_vigencia_apto.day, hour=23, minute=59, second=59)
        },
        'sportaccess_id': f"MUVI-{documento}",
        'poi': {
            'installments': payment['installments'],
            'payment_reference': payment['id']
        }
    }

    # * Dates

    plan = db.planes.find_one({'_id': plan})
    npd = calculate_payment_date(today.day, plan['cobro'], get_periodo(today))
    socio['next_payment_date'] = npd
    socio['fecha_vigencia'] = set_next_vigency(npd)
    socio['last_subscription_date'] = today
    socio['period_init_day'] = today.day

    # * Customer mp

    customer_response = sdk.customer().search({'email': email})['response']
    if customer_response['paging']['total'] == 1:
        customer = customer_response['results'][0]
        customer_id = customer['id']
    else:
        customer_data = {
            "email": email,
            "first_name": nombre,
            "last_name": apellido,
            "phone": {"area_code": None, "number": celular},
            'identification': {'type': 'DNI', 'number': documento},
            'address': {
                'street_name': calle,
                'street_number': altura,
            }
        }
        customer = sdk.customer().create(customer_data)['response']
        if 'email' in customer.keys():
            customer_id = customer['id']
        else:
            customer_id = 'error'

    socio['mercadopago_id'] = customer_id

    # * History

    history_event = create_history_event(
        member=socio, event_type='alta', source='checkout')
    socio['history'] = [history_event]

    # * Plan corporativo

    if plan['price'] == payment['transaction_amount']:
        socio['plan_corporativo'] = None
        plan['corporativo'] = None
    else:
        abandoned = db.abandoned.find_one({'documento': documento})
        try:
            socio['plan_corporativo'] = abandoned['corpo_id']
        except:
            # * No hay forma de recuperar el corporativo que le aplicó un descuento
            return

    return socio

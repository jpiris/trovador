from django.dispatch import receiver

from django_registration.signals import user_activated
from django_registration.backends.activation.views import ActivationView

from catalogo.models import User

import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = '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'

api_instance = sib_api_v3_sdk.ContactsApi(sib_api_v3_sdk.ApiClient(configuration))

@receiver(user_activated, sender=ActivationView, dispatch_uid='django_registration.signals.user_activated')
def nuevo_usuario_activado_handler(user, **kwargs):
    print("aqui " + user.email)
    
    create_contact = sib_api_v3_sdk.CreateContact(email=user.email)

    try:
        api_response = api_instance.create_contact(create_contact)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactsApi->create_contact: %s\n" % e)
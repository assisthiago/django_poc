from django.contrib import admin, messages

from twilio.rest import Client

from .models import Patient


@admin.action(description='Mandar mensagem pelo Whatsapp')
def send_whatsapp_message(modeladmin, request, queryset):
    client = Client()
    client.messages.create(
        body='Olá, aqui é o oftalmo.',
        from_='whatsapp:+14155238886',
        to=f'whatsapp:+55{queryset[0].phone_number}'
    )

    messages.success(request, 'A mensagem pelo Whatsapp foi enviada com sucesso.')



@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'name', 'phone_number', 'birthdate',)

    actions = [send_whatsapp_message]


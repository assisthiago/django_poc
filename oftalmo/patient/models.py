from django.db import models


class Patient(models.Model):
    cpf = models.BigIntegerField(primary_key=True, verbose_name='CPF')
    name = models.CharField(max_length=255, verbose_name='Nome')
    birthdate = models.DateField(verbose_name='Nascimento')
    phone_number = models.BigIntegerField(verbose_name='Telefone')
    email = models.CharField(max_length=255, verbose_name='E-mail')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'paciente'
        verbose_name_plural = 'Pacientes'

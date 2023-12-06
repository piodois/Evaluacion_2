from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator

class Reserva(models.Model):
    ESTADOS_RESERVA = (
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO_ASISTEN', 'No Asisten'),
    )

    nombre = models.CharField(max_length=80)
    telefono = models.CharField(max_length=15)
    fecha_reserva = models.DateField()
    hora_reserva = models.TimeField()
    cantidad_personas = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(15)])
    correo = models.EmailField(validators=[EmailValidator()])
    estado = models.CharField(max_length=20, choices=ESTADOS_RESERVA)
    observacion = models.TextField(blank=True, null=True)
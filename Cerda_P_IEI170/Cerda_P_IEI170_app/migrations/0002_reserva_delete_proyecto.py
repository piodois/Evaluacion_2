

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cerda_P_IEI170_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('telefono', models.CharField(max_length=15)),
                ('fecha_reserva', models.DateField()),
                ('hora_reserva', models.TimeField()),
                ('cantidad_personas', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(15)])),
                ('correo', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()])),
                ('estado', models.CharField(choices=[('RESERVADO', 'Reservado'), ('COMPLETADA', 'Completada'), ('ANULADA', 'Anulada'), ('NO_ASISTEN', 'No Asisten')], max_length=20)),
                ('observacion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Proyecto',
        ),
    ]

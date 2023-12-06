

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechainicio', models.DateField()),
                ('fechatermino', models.DateField()),
                ('nombre', models.CharField(max_length=50)),
                ('responsable', models.CharField(max_length=50)),
                ('prioriodad', models.IntegerField()),
            ],
        ),
    ]

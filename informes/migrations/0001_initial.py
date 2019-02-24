# Generated by Django 2.1.5 on 2019-02-24 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Informe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('texto', models.CharField(max_length=10000, verbose_name='Texto')),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Informe',
                'verbose_name_plural': 'Informes',
            },
        ),
    ]

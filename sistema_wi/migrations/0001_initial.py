# Generated by Django 2.1.5 on 2019-02-06 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ValoresEstaticos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano_wi', models.CharField(default='29', max_length=5)),
                ('nome_wifi', models.CharField(default='polijunior', max_length=100)),
                ('senha_wifi', models.CharField(default='polijunior', max_length=100)),
                ('data_de_inicio', models.DateField(default=None)),
            ],
            options={
                'verbose_name': 'Valores Estaticos',
                'verbose_name_plural': 'Valores Estaticos',
            },
        ),
    ]

# Generated by Django 2.1.5 on 2019-02-28 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dataFeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(blank=True, null=True, verbose_name='data')),
                ('dataCriado', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'dataFeed',
                'verbose_name_plural': 'dataFeeds',
            },
        ),
        migrations.CreateModel(
            name='LinkFeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=1000, null=True, verbose_name='nome')),
                ('link', models.CharField(blank=True, max_length=1000, null=True, verbose_name='link')),
            ],
            options={
                'verbose_name': 'Link de Feedback',
                'verbose_name_plural': 'Links de Feedback',
            },
        ),
        migrations.CreateModel(
            name='ValoresEstaticos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano_wi', models.CharField(default='29', max_length=5)),
                ('nome_wifi', models.CharField(default='polijunior', max_length=100)),
                ('senha_wifi', models.CharField(default='polijunior', max_length=100)),
                ('data_de_inicio', models.DateField(default=None)),
                ('mapa_wi', models.FileField(blank=True, null=True, upload_to='sistema_wi/fotos')),
                ('calendario_wi', models.FileField(blank=True, null=True, upload_to='sistema_wi/fotos')),
                ('horario_massagem_inicio', models.TimeField()),
                ('horario_massagem_fim', models.TimeField()),
                ('intervalo_massagem', models.IntegerField()),
                ('n_salas', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Valores Estaticos',
                'verbose_name_plural': 'Valores Estaticos',
            },
        ),
    ]

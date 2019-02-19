# Generated by Django 2.1.5 on 2019-02-19 02:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Caravaneiro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('stand', models.IntegerField()),
                ('tamanho', models.IntegerField(choices=[(0, '9 m2'), (1, '10 m2'), (2, '10,5 m2'), (3, '12 m2'), (4, '14 m2'), (5, '20 m2'), (6, '25,5 m2'), (7, '30 m2'), (8, '40 m2'), (9, '51,5 m2')])),
                ('palestra', models.BooleanField(default=False)),
                ('cnpj', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Gerente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Organizador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
            options={
                'verbose_name': 'Organizador',
                'verbose_name_plural': 'Organizadores',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.IntegerField(choices=[(0, 'Empresa'), (1, 'Organizador'), (2, 'Gerente'), (3, 'Caravaneiro')])),
                ('enviou_mensagem', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='organizador',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_organizador', to='usuarios.Usuario'),
        ),
        migrations.AddField(
            model_name='gerente',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_gerente', to='usuarios.Usuario'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='organizador_resp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empresa_organizador', to='usuarios.Organizador'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_empresa', to='usuarios.Usuario'),
        ),
        migrations.AddField(
            model_name='caravaneiro',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_caravaneiro', to='usuarios.Usuario'),
        ),
    ]

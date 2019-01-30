# Generated by Django 2.1.5 on 2019-01-30 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True, null=True)),
                ('observacao', models.TextField(blank=True, max_length=200, verbose_name='Observação')),
                ('organizador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Organizador')),
                ('pedinte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Empresa')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nome')),
                ('image', models.ImageField(blank=True, null=True, upload_to='pedidos/images', verbose_name='Imagem')),
            ],
            options={
                'verbose_name': 'Tipo de Pedido',
                'verbose_name_plural': 'Tipos de Pedido',
            },
        ),
        migrations.AddField(
            model_name='pedido',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.Type'),
        ),
    ]

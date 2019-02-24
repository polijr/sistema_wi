# Generated by Django 2.1.5 on 2019-02-24 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('documentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotaFiscal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('arquivo', models.FileField(upload_to='documentos/files')),
                ('observacao', models.TextField(blank=True, max_length=200, verbose_name='observacao')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nota_empresa', to='usuarios.Empresa')),
            ],
        ),
    ]

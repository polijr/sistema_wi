# Generated by Django 2.1.5 on 2019-02-04 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [

    ]
    

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('arquivo', models.FileField(upload_to='documentos/files')),
                ('observacao', models.TextField(max_length=200, verbose_name='Observação')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arquivo_empresa', to='usuarios.Empresa')),
            ],
        ),
    ]

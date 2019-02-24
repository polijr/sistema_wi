# Generated by Django 2.1.5 on 2019-02-24 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(max_length=200, verbose_name='Mensagem')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('recebeu', models.BooleanField(default=False)),
                ('emissor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensagens_emitidas', to='usuarios.Usuario')),
                ('receptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensagens_recebidas', to='usuarios.Usuario')),
            ],
            options={
                'verbose_name': 'Mensagem',
                'verbose_name_plural': 'Mensagens',
            },
        ),
    ]

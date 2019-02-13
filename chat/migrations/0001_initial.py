# Generated by Django 2.1.4 on 2019-02-11 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0002_auto_20190206_2039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(max_length=200, verbose_name='Mensagem')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('emissor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensagens_emitidas', to='usuarios.Usuario')),
                ('receptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensagens_recebidas', to='usuarios.Usuario')),
            ],
            options={
                'verbose_name': 'Mensagem',
                'verbose_name_plural': 'Mensagens',
            },
        ),
    ]
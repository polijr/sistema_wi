# Generated by Django 2.0 on 2019-01-25 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20190124_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='nome',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]

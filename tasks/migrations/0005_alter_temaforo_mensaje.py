# Generated by Django 4.2.7 on 2023-12-10 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_temaforo_mensaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temaforo',
            name='mensaje',
            field=models.TextField(default=''),
        ),
    ]

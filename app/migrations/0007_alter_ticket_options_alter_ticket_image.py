# Generated by Django 4.2.1 on 2023-05-28 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_user_ticket'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={},
        ),
        migrations.AlterField(
            model_name='ticket',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]

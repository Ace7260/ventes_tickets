# Generated by Django 4.2.1 on 2023-05-28 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_ticket_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='code',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]

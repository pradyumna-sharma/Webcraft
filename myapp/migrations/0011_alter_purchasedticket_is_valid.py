# Generated by Django 3.2.6 on 2023-11-18 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_purchasedticket_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasedticket',
            name='is_valid',
            field=models.BooleanField(default=True),
        ),
    ]
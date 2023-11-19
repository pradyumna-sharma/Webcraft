# Generated by Django 3.2.6 on 2023-11-15 06:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_rename_event_name_purchasedticket_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasedticket',
            name='is_valid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='purchasedticket',
            name='token',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]

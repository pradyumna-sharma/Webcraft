# Generated by Django 4.2.7 on 2023-11-23 02:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0013_alter_gallery_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gallery",
            name="photo",
            field=models.ImageField(upload_to="static/image/"),
        ),
    ]
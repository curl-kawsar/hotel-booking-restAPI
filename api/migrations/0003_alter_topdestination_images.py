# Generated by Django 5.0.4 on 2024-09-17 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_room_accommodates_room_is_ac_room_number_of_beds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topdestination',
            name='images',
            field=models.TextField(),
        ),
    ]

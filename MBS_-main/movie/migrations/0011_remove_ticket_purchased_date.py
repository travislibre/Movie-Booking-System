# Generated by Django 4.2 on 2023-04-23 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0010_showtime_ticket_theatre_showtime_theatre_showing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='purchased_date',
        ),
    ]
# Generated by Django 3.2.7 on 2021-10-04 05:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_board_up'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='c_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 4, 5, 35, 17, 843568, tzinfo=utc)),
        ),
    ]

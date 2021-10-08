# Generated by Django 3.2.7 on 2021-10-04 05:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vote', '0002_alter_choice_cuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='c_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='voter',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]

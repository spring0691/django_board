# Generated by Django 3.2.7 on 2021-09-24 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='subject',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='board',
            name='writer',
            field=models.CharField(max_length=30),
        ),
    ]

# Generated by Django 5.1.7 on 2025-04-01 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='isborrowed',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 5.1.7 on 2025-04-03 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_isborrowed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]

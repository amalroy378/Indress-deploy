# Generated by Django 4.1.7 on 2023-03-22 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_carousel_home_carousel_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel_home',
            name='carousel_text',
            field=models.CharField(max_length=200),
        ),
    ]
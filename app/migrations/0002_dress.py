# Generated by Django 4.1.7 on 2023-02-20 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dress_img', models.ImageField(upload_to='photos')),
                ('dress_name', models.CharField(max_length=200)),
            ],
        ),
    ]

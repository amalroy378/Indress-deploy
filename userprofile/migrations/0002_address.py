# Generated by Django 4.1.7 on 2023-03-27 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('house_name', models.CharField(max_length=150)),
                ('delivery_instruction', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('default', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
        ),
    ]
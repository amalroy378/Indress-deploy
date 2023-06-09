# Generated by Django 4.1.7 on 2023-03-21 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eachcategorypages', '0003_alter_product_slug_productimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='img')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='eachcategorypages.product')),
            ],
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]

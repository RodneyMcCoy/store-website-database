# Generated by Django 4.0.4 on 2022-04-20 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_bundle_customer_product_service_vendor_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bundle',
            name='bundle_id',
            field=models.IntegerField(verbose_name='bundle_id'),
        ),
        migrations.AlterField(
            model_name='bundle',
            name='vendor_id',
            field=models.IntegerField(verbose_name='vendor_id'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.IntegerField(verbose_name='customer_id'),
        ),
        migrations.AlterField(
            model_name='product',
            name='bundle_id',
            field=models.IntegerField(verbose_name='bundle_id'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.IntegerField(verbose_name='product_id'),
        ),
        migrations.AlterField(
            model_name='product',
            name='vendor_id',
            field=models.IntegerField(verbose_name='vendor_id'),
        ),
        migrations.AlterField(
            model_name='service',
            name='bundle_id',
            field=models.IntegerField(verbose_name='bundle_id'),
        ),
        migrations.AlterField(
            model_name='service',
            name='service_id',
            field=models.IntegerField(verbose_name='service_id'),
        ),
        migrations.AlterField(
            model_name='service',
            name='vendor_id',
            field=models.IntegerField(verbose_name='vendor_id'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vendor_id',
            field=models.IntegerField(verbose_name='vendor_id'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='customer_id',
            field=models.IntegerField(verbose_name='customer_id'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='product_id',
            field=models.IntegerField(verbose_name='product_id'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='service_id',
            field=models.IntegerField(verbose_name='service_id'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='wishlist_id',
            field=models.IntegerField(verbose_name='wishlist_id'),
        ),
    ]

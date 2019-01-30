# Generated by Django 2.1.3 on 2018-12-27 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0004_auto_20181224_1755'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_life', models.IntegerField(choices=[(30, '30天'), (60, '60天'), (180, '180天'), (360, '360天'), (720, '720天')])),
                ('price', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_product', models.CharField(max_length=4)),
                ('name_of_product', models.CharField(max_length=20)),
                ('value_added_tax_rate', models.CharField(max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='price',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.Product'),
        ),
    ]

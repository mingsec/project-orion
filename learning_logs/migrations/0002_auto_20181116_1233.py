# Generated by Django 2.1.3 on 2018-11-16 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_modify',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

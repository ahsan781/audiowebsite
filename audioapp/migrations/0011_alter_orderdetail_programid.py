# Generated by Django 3.2.8 on 2021-11-04 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audioapp', '0010_orderdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='ProgramID',
            field=models.CharField(max_length=300),
        ),
    ]

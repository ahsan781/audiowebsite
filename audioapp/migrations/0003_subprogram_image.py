# Generated by Django 3.2.8 on 2021-10-23 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audioapp', '0002_alter_program_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='subprogram',
            name='image',
            field=models.FileField(null=True, upload_to='images/'),
        ),
    ]
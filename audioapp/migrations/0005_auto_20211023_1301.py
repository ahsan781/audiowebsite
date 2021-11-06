# Generated by Django 3.2.8 on 2021-10-23 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('audioapp', '0004_subprogram_artistname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subprogram',
            name='artistname',
        ),
        migrations.RemoveField(
            model_name='subprogram',
            name='audiofile',
        ),
        migrations.RemoveField(
            model_name='subprogram',
            name='audioname',
        ),
        migrations.RemoveField(
            model_name='subprogram',
            name='image',
        ),
        migrations.RemoveField(
            model_name='subprogram',
            name='price',
        ),
        migrations.CreateModel(
            name='audio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('audioname', models.CharField(max_length=200)),
                ('artistname', models.CharField(max_length=200, null=True)),
                ('image', models.FileField(null=True, upload_to='images/')),
                ('audiofile', models.FileField(null=True, upload_to='audio/')),
                ('price', models.IntegerField()),
                ('subprogram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audioapp.subprogram')),
            ],
        ),
    ]

# Generated by Django 4.0 on 2021-12-20 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='image',
            field=models.CharField(default='https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='image',
            field=models.CharField(default='https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artwork',
            name='image',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='medium',
            field=models.CharField(max_length=255),
        ),
    ]

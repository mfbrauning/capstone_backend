# Generated by Django 4.0 on 2021-12-18 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=50)),
                ('dob', models.CharField(max_length=50)),
                ('movement', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('medium', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=255)),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='artworks', to='art.artist')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='artworks', to='art.location')),
            ],
        ),
    ]
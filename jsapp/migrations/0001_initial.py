# Generated by Django 5.0.6 on 2024-06-17 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='coursesavedb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Course Image')),
            ],
        ),
    ]

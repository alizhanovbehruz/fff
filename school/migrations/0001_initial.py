# Generated by Django 4.2.1 on 2023-05-06 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=13)),
                ('description', models.TextField(blank=True)),
                ('data_create', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Bildirishnoma',
                'verbose_name_plural': 'Bildirishnomalar',
                'ordering': ('-data_create',),
            },
        ),
    ]

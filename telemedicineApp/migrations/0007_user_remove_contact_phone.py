# Generated by Django 4.0 on 2024-12-22 07:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('telemedicineApp', '0006_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
    ]

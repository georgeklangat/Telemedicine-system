# Generated by Django 4.0 on 2024-12-16 07:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('telemedicineApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]

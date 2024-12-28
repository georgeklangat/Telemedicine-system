# Generated by Django 4.0 on 2024-12-16 08:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('telemedicineApp', '0003_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('department', models.CharField(max_length=100)),
                ('doctor', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
    ]
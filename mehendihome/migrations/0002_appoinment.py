# Generated by Django 4.0.6 on 2022-08-14 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mehendihome', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='appoinment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('address', models.CharField(max_length=122)),
                ('time', models.DateTimeField()),
                ('number', models.CharField(max_length=122)),
            ],
        ),
    ]
# Generated by Django 4.0.6 on 2022-08-14 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mehendi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('mehendi_style', models.CharField(max_length=122)),
                ('mehendi_desc', models.CharField(max_length=122)),
                ('mehendi_time', models.TimeField()),
                ('image', models.ImageField(upload_to='mehendi/images')),
                ('mehendi_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='rangoli',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('rangoli_style', models.CharField(max_length=122)),
                ('rangoli_desc', models.CharField(max_length=122)),
                ('rangoli_date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='rangoli/images')),
            ],
        ),
    ]

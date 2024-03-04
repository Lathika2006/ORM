# Generated by Django 5.0.2 on 2024-02-27 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book_Details',
            fields=[
                ('Book_name', models.CharField(max_length=100)),
                ('Book_serial_number', models.IntegerField(primary_key='Book_serial_number', serialize=False)),
                ('author_name', models.CharField(max_length=30)),
                ('No_of_pages', models.IntegerField()),
                ('Genre', models.CharField(max_length=100)),
                ('No_of_Characters', models.IntegerField()),
                ('No_of_Chapters', models.IntegerField()),
                ('Year', models.IntegerField(help_text='Published', max_length=4)),
            ],
        ),
    ]

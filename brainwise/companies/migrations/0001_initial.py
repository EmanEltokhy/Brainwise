# Generated by Django 5.1.4 on 2024-12-08 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('number_of_departments', models.PositiveIntegerField(default=0, editable=False)),
                ('number_of_employees', models.PositiveIntegerField(default=0, editable=False)),
            ],
        ),
    ]

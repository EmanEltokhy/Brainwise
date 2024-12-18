# Generated by Django 5.1.4 on 2024-12-08 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_alter_employee_mobile_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='status',
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='stage',
            field=models.CharField(choices=[('application_received', 'Application Received'), ('interview_scheduled', 'Interview Scheduled'), ('hired', 'Hired'), ('not_accepted', 'Not Accepted')], default='application_received', max_length=20),
        ),
        migrations.AddField(
            model_name='employee',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.CharField(editable=False, max_length=200),
        ),
    ]

# Generated by Django 2.2.7 on 2021-03-02 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20210302_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_address',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_position',
            field=models.CharField(choices=[('team_lead', 'Team Lead'), ('project_manager', 'Project Manager'), ('software_engineer', 'Software Engineer'), ('tester', 'Tester')], default='software_engineer', max_length=30),
        ),
    ]
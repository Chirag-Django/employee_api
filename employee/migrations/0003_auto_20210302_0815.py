# Generated by Django 2.2.7 on 2021-03-02 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20210302_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_no',
            field=models.IntegerField(unique=True),
        ),
    ]

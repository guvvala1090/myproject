# Generated by Django 3.1.7 on 2021-04-06 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20210406_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_data',
            name='gender',
            field=models.CharField(max_length=7, null=True),
        ),
    ]

# Generated by Django 3.1.1 on 2020-09-28 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Groups', '0022_student_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(default='No data'),
        ),
    ]

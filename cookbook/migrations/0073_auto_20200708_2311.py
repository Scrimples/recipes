# Generated by Django 3.0.7 on 2020-07-08 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0072_step_show_as_header'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sync',
            name='last_checked',
            field=models.DateTimeField(null=True),
        ),
    ]
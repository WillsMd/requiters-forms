# Generated by Django 4.2 on 2024-11-23 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recuitz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='clubs',
            field=models.JSONField(blank=True, default=dict, help_text='Choose the list of clubs you are in.', null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='skills',
            field=models.JSONField(default=dict, help_text="Provide a list of your skills (e.g., ['Python', 'Django', 'React'])."),
        ),
    ]

# Generated by Django 5.1.1 on 2024-09-21 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_url_full_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='counter',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

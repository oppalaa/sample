# Generated by Django 4.2.1 on 2023-06-30 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_webpage_acessrecord'),
    ]

    operations = [
        migrations.RenameField(
            model_name='webpage',
            old_name='top_name',
            new_name='topic_name',
        ),
    ]

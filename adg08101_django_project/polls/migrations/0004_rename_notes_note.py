# Generated by Django 3.2 on 2021-04-21 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_notes_question'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notes',
            new_name='Note',
        ),
    ]

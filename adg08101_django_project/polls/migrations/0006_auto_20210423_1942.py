# Generated by Django 3.2 on 2021-04-23 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_rename_note_note_note_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='question',
        ),
        migrations.AddField(
            model_name='note',
            name='question',
            field=models.ManyToManyField(to='polls.Question'),
        ),
    ]
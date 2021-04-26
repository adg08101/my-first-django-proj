# Generated by Django 3.2 on 2021-04-21 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll_app', '0002_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='question',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='poll_app.question'),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.2 on 2021-05-13 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll_app', '0037_alter_questiontype_question_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questiontype',
            name='question_type',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='poll_app.question'),
            preserve_default=True,
        ),
    ]

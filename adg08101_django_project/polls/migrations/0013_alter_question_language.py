# Generated by Django 3.2 on 2021-04-24 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_alter_question_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='language',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.language'),
            preserve_default=True,
        ),
    ]

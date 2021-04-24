# Generated by Django 3.2 on 2021-04-24 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls_app', '0017_alter_question_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='language',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='polls_app.language'),
            preserve_default=True
        ),
    ]

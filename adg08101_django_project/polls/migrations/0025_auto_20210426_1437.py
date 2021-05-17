# Generated by Django 3.2 on 2021-04-26 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0024_alter_question_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questiontype',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.ManyToManyField(to='polls.QuestionType'),
        ),
    ]
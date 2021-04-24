# Generated by Django 3.2 on 2021-04-23 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls_app', '0006_auto_20210423_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_text', models.CharField(max_length=150)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('question', models.ManyToManyField(to='polls_app.Question')),
            ],
        ),
        migrations.DeleteModel(
            name='Note',
        ),
    ]

# Generated by Django 3.2 on 2021-04-23 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll_app', '0007_auto_20210423_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_text', models.CharField(max_length=150)),
                ('pub_date', models.DateTimeField(verbose_name='date created')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll_app.question')),
            ],
        ),
    ]
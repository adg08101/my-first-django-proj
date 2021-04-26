# Generated by Django 3.2 on 2021-04-26 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll_app', '0027_auto_20210426_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='choice',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='poll_app.choice'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='language',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='poll_app.language'),
            preserve_default=True,
        ),
    ]

# Generated by Django 3.2 on 2021-04-26 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0026_auto_20210426_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='choice',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.choice'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='language',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.language'),
            preserve_default=True,
        ),
    ]

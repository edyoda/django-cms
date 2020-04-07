# Generated by Django 2.2.10 on 2020-04-07 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200407_1627'),
        ('blog', '0008_auto_20200331_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.Profile'),
            preserve_default=False,
        ),
    ]
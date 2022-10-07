# Generated by Django 4.1.1 on 2022-10-03 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translate', '0002_alter_languagesmodel_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votesmodel',
            name='type',
        ),
        migrations.AddField(
            model_name='votesmodel',
            name='rating',
            field=models.SmallIntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='votesmodel',
            name='date_time',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='votesmodel',
            name='ip',
            field=models.TextField(blank=True),
        ),
    ]

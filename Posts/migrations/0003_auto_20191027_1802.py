# Generated by Django 2.2.6 on 2019-10-27 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0002_auto_20191027_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.IntegerField(choices=[(0, 'Breaking news'), (1, 'Followup'), (2, 'Just kidding')]),
        ),
    ]
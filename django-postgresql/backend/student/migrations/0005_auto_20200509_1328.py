# Generated by Django 3.0.5 on 2020-05-09 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20200504_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='subj1_att',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='subj2_att',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='subj3_att',
            field=models.IntegerField(null=True),
        ),
    ]

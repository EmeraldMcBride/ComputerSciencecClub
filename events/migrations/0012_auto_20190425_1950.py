# Generated by Django 2.1.5 on 2019-04-25 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20190425_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepageevent',
            name='age_requirement',
            field=models.CharField(max_length=200),
        ),
    ]

# Generated by Django 4.0.4 on 2022-04-20 00:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_schedulehours_horarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulehours',
            name='horarios',
            field=models.CharField(choices=[('09:00', datetime.time(9, 0)), ('10:00', datetime.time(10, 0)), ('11:00', datetime.time(11, 0)), ('13:00', datetime.time(13, 0)), ('14:00', datetime.time(14, 0)), ('15:00', datetime.time(15, 0)), ('16:00', datetime.time(16, 0)), ('17:00', datetime.time(17, 0))], max_length=5, unique=True),
        ),
    ]

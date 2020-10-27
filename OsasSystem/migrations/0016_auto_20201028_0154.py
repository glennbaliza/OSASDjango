# Generated by Django 3.0 on 2020-10-27 17:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('OsasSystem', '0015_auto_20201028_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osas_r_emergency_contact',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 17, 54, 2, 466839, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_r_emergency_contact',
            name='date_updated',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 17, 54, 2, 466839, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_r_personal_info',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 17, 54, 2, 466839, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_r_personal_info',
            name='date_updated',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 17, 54, 2, 466839, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_r_stud_contact',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 17, 54, 2, 466839, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_r_stud_contact',
            name='date_updated',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 17, 54, 2, 466839, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_r_userrole',
            name='user_type',
            field=models.CharField(max_length=50, verbose_name='User Type'),
        ),
        migrations.AlterField(
            model_name='osas_t_id',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 17, 54, 2, 466839, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_t_id',
            name='date_updated',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 17, 54, 2, 466839, tzinfo=utc)),
        ),
    ]

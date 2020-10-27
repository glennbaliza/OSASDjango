# Generated by Django 3.0 on 2020-10-27 17:32

import OsasSystem.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('OsasSystem', '0014_auto_20201027_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osas_r_emergency_contact',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 17, 32, 45, 17221, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_r_emergency_contact',
            name='date_updated',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 17, 32, 45, 17221, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_r_personal_info',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 17, 32, 45, 17221, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_r_personal_info',
            name='date_updated',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 17, 32, 45, 17221, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_r_stud_contact',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 17, 32, 45, 17221, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_r_stud_contact',
            name='date_updated',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 17, 32, 45, 17221, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_r_userrole',
            name='s_image',
            field=models.ImageField(default='profile_pic.png', upload_to=OsasSystem.models.image_path),
        ),
        migrations.AlterField(
            model_name='osas_t_id',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 17, 32, 45, 17221, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_t_id',
            name='date_updated',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 17, 32, 45, 17221, tzinfo=utc)),
        ),
    ]

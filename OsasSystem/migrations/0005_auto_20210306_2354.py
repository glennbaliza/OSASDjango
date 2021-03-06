# Generated by Django 3.0 on 2021-03-06 15:54

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('OsasSystem', '0004_auto_20210306_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='osas_notif',
            name='notif_stud_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='OsasSystem.osas_r_personal_info'),
        ),
        migrations.AlterField(
            model_name='osas_notif',
            name='notif_datecreated',
            field=models.DateField(default=datetime.datetime(2021, 3, 6, 15, 54, 28, 583487, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_r_auth_user',
            name='date_updated',
            field=models.DateField(default=datetime.datetime(2021, 3, 6, 15, 54, 28, 583487, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_r_code_title',
            name='ct_datecreated',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 6, 15, 54, 28, 583487, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_r_course',
            name='course_add_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 6, 15, 54, 28, 583487, tzinfo=utc), max_length=50),
        ),
        migrations.AlterField(
            model_name='osas_r_course',
            name='course_edit_date',
            field=models.DateField(default=datetime.datetime(2021, 3, 6, 15, 54, 28, 583487, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_r_designation_office',
            name='designation_datecreated',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 6, 15, 54, 28, 583487, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_r_disciplinary_sanction',
            name='ds_datecreated',
            field=models.DateField(default=datetime.datetime(2021, 3, 6, 15, 54, 28, 583487, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='osas_r_personal_info',
            name='date_updated',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 6, 15, 54, 28, 583487, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_r_personal_info',
            name='stud_birthdate',
            field=models.DateField(default=datetime.datetime(2021, 3, 6, 15, 54, 28, 583487, tzinfo=utc), max_length=12),
        ),
        migrations.AlterField(
            model_name='osas_r_section_and_year',
            name='yas_dateregistered',
            field=models.DateField(default=datetime.datetime(2021, 3, 6, 15, 54, 28, 583487, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_r_userrole',
            name='date_updated',
            field=models.DateField(default=datetime.datetime(2021, 3, 6, 15, 54, 28, 583487, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_t_complaint',
            name='comp_datecreated',
            field=models.DateField(default=datetime.datetime(2021, 3, 6, 15, 54, 28, 583487, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_t_excuse',
            name='excuse_datecreated',
            field=models.DateField(default=datetime.datetime(2021, 3, 6, 15, 54, 28, 583487, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_t_excuse',
            name='excuse_dateupdated',
            field=models.DateField(default=datetime.datetime(2021, 3, 6, 15, 54, 28, 583487, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_t_sanction',
            name='sanction_dateupdated',
            field=models.DateField(default=datetime.datetime(2021, 3, 6, 15, 54, 28, 583487, tzinfo=utc)),
        ),
    ]

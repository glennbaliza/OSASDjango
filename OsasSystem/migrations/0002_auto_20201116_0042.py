# Generated by Django 3.0 on 2020-11-15 16:42

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('OsasSystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osas_r_auth_user',
            name='date_updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 15, 16, 42, 55, 572712, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_r_competencies',
            name='comp_updateddate',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 15, 16, 42, 55, 572712, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_r_course',
            name='course_edit_date',
            field=models.DateField(default=datetime.datetime(2020, 11, 15, 16, 42, 55, 572712, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_r_educ',
            name='educ_graduation_date',
            field=models.DateField(default=datetime.datetime(2020, 11, 15, 16, 42, 55, 572712, tzinfo=utc), max_length=12),
        ),
        migrations.AlterField(
            model_name='osas_r_educ',
            name='educ_updatedteddate',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 15, 16, 42, 55, 572712, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_r_employ',
            name='employ_date1st_employ',
            field=models.DateField(default=datetime.datetime(2020, 11, 15, 16, 42, 55, 572712, tzinfo=utc), max_length=12),
        ),
        migrations.AlterField(
            model_name='osas_r_employ',
            name='employ_date_current',
            field=models.DateField(default=datetime.datetime(2020, 11, 15, 16, 42, 55, 572712, tzinfo=utc), max_length=12),
        ),
        migrations.AlterField(
            model_name='osas_r_employ',
            name='employ_updatedddate',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 15, 16, 42, 55, 572712, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_r_personal_info',
            name='date_updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 15, 16, 42, 55, 572712, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_r_personal_info',
            name='stud_birthdate',
            field=models.DateField(default=datetime.datetime(2020, 11, 15, 16, 42, 55, 572712, tzinfo=utc), max_length=12),
        ),
        migrations.AlterField(
            model_name='osas_r_rate',
            name='rate_updatedddate',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 15, 16, 42, 55, 572712, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_r_referral',
            name='ref_date_updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 15, 16, 42, 55, 572712, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_r_relevant',
            name='rel_updatedddate',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 15, 16, 42, 55, 572712, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_r_section_and_year',
            name='yas_dateregistered',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 15, 16, 42, 55, 572712, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_r_userrole',
            name='date_updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 15, 16, 42, 55, 572712, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='osas_t_profile',
            name='prof_updateddate',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 15, 16, 42, 55, 572712, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='osas_t_id',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(max_length=50)),
                ('date_updated', models.DateTimeField(default=datetime.datetime(2020, 11, 15, 16, 42, 55, 572712, tzinfo=utc))),
                ('lost_id_status', models.CharField(default='Pending', max_length=13)),
                ('lost_stud_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OsasSystem.osas_r_personal_info')),
            ],
        ),
    ]
# Generated by Django 5.1.1 on 2024-09-15 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterUnit',
            fields=[
                ('masterunitid', models.AutoField(db_column='masterUnitID', primary_key=True, serialize=False)),
                ('unitname', models.TextField(db_column='unitName')),
            ],
            options={
                'db_table': 'master_unit',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OtherUnit',
            fields=[
                ('otherunitid', models.AutoField(db_column='otherUnitID', primary_key=True, serialize=False)),
                ('unitname', models.TextField(db_column='unitName')),
            ],
            options={
                'db_table': 'other_unit',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('uid', models.TextField(db_column='UID', primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('showunit', models.TextField(blank=True, db_column='showUnit', null=True)),
                ('discountinfo', models.TextField(blank=True, db_column='discountInfo', null=True)),
                ('descriptionfilterhtml', models.TextField(blank=True, db_column='descriptionFilterHtml', null=True)),
                ('imageurl', models.TextField(blank=True, db_column='imageUrl', null=True)),
                ('websales', models.TextField(blank=True, db_column='webSales', null=True)),
                ('sourcewebpromote', models.TextField(blank=True, db_column='sourceWebPromote', null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('editmodifydate', models.DateTimeField(blank=True, db_column='editModifyDate', null=True)),
                ('startdate', models.DateTimeField(db_column='startDate')),
                ('enddate', models.DateTimeField(db_column='endDate')),
                ('hitrate', models.IntegerField(db_column='hitRate')),
                ('version', models.TextField()),
            ],
            options={
                'db_table': 'show',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ShowInfo',
            fields=[
                ('showinfoid', models.AutoField(db_column='showInfoID', primary_key=True, serialize=False)),
                ('time', models.DateTimeField()),
                ('location', models.TextField()),
                ('locationname', models.TextField(db_column='locationName')),
                ('onsales', models.TextField(db_column='onSales')),
                ('price', models.TextField(blank=True, null=True)),
                ('latitude', models.TextField(blank=True, null=True)),
                ('longitude', models.TextField(blank=True, null=True)),
                ('endtime', models.DateTimeField(db_column='endTime')),
            ],
            options={
                'db_table': 'show_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SourceWeb',
            fields=[
                ('sourcewebid', models.AutoField(db_column='sourceWebID', primary_key=True, serialize=False)),
                ('sourcewebname', models.TextField(db_column='sourceWebName')),
            ],
            options={
                'db_table': 'source_web',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SubUnit',
            fields=[
                ('subunitid', models.AutoField(db_column='subUnitID', primary_key=True, serialize=False)),
                ('unitname', models.TextField(db_column='unitName')),
            ],
            options={
                'db_table': 'sub_unit',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SupportUnit',
            fields=[
                ('supportunitid', models.AutoField(db_column='supportUnitID', primary_key=True, serialize=False)),
                ('unitname', models.TextField(db_column='unitName')),
            ],
            options={
                'db_table': 'support_unit',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'managed': False},
        ),
    ]

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Category(models.Model):
    categoryid = models.AutoField(db_column='categoryID', primary_key=True)  # Field name made lowercase.
    categoryname = models.TextField(db_column='categoryName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'category'


class MasterUnit(models.Model):
    masterunitid = models.AutoField(db_column='masterUnitID', primary_key=True)  # Field name made lowercase.
    uid = models.ForeignKey('Show', models.DO_NOTHING, db_column='UID')  # Field name made lowercase.
    unitname = models.TextField(db_column='unitName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'master_unit'


class OtherUnit(models.Model):
    otherunitid = models.AutoField(db_column='otherUnitID', primary_key=True)  # Field name made lowercase.
    uid = models.ForeignKey('Show', models.DO_NOTHING, db_column='UID')  # Field name made lowercase.
    unitname = models.TextField(db_column='unitName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'other_unit'


class Show(models.Model):
    uid = models.TextField(db_column='UID', primary_key=True)  # Field name made lowercase.
    title = models.TextField()
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='category')
    showunit = models.TextField(db_column='showUnit', blank=True, null=True)  # Field name made lowercase.
    discountinfo = models.TextField(db_column='discountInfo', blank=True, null=True)  # Field name made lowercase.
    descriptionfilterhtml = models.TextField(db_column='descriptionFilterHtml', blank=True, null=True)  # Field name made lowercase.
    imageurl = models.TextField(db_column='imageUrl', blank=True, null=True)  # Field name made lowercase.
    websales = models.TextField(db_column='webSales', blank=True, null=True)  # Field name made lowercase.
    sourcewebpromote = models.TextField(db_column='sourceWebPromote', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(blank=True, null=True)
    editmodifydate = models.TextField(db_column='editModifyDate', blank=True, null=True)  # Field name made lowercase.
    sourcewebid = models.ForeignKey('SourceWeb', models.DO_NOTHING, db_column='sourceWebID')  # Field name made lowercase.
    startdate = models.TextField(db_column='startDate')  # Field name made lowercase.
    enddate = models.TextField(db_column='endDate')  # Field name made lowercase.
    hitrate = models.IntegerField(db_column='hitRate')  # Field name made lowercase.
    version = models.TextField()

    class Meta:
        managed = False
        db_table = 'show'


class ShowInfo(models.Model):
    showinfoid = models.AutoField(db_column='showInfoID', primary_key=True)  # Field name made lowercase.
    uid = models.ForeignKey(Show, models.DO_NOTHING, db_column='UID')  # Field name made lowercase.
    time = models.TextField()
    location = models.TextField()
    locationname = models.TextField(db_column='locationName')  # Field name made lowercase.
    onsales = models.TextField(db_column='onSales')  # Field name made lowercase.
    price = models.TextField(blank=True, null=True)
    latitude = models.TextField(blank=True, null=True)
    longitude = models.TextField(blank=True, null=True)
    endtime = models.TextField(db_column='endTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'show_info'


class SourceWeb(models.Model):
    sourcewebid = models.AutoField(db_column='sourceWebID', primary_key=True)  # Field name made lowercase.
    sourcewebname = models.TextField(db_column='sourceWebName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'source_web'


class SubUnit(models.Model):
    subunitid = models.AutoField(db_column='subUnitID', primary_key=True)  # Field name made lowercase.
    uid = models.ForeignKey(Show, models.DO_NOTHING, db_column='UID')  # Field name made lowercase.
    unitname = models.TextField(db_column='unitName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sub_unit'


class SupportUnit(models.Model):
    supportunitid = models.AutoField(db_column='supportUnitID', primary_key=True)  # Field name made lowercase.
    uid = models.ForeignKey(Show, models.DO_NOTHING, db_column='UID')  # Field name made lowercase.
    unitname = models.TextField(db_column='unitName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'support_unit'

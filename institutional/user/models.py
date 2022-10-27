from distutils.sysconfig import customize_compiler
from django.db import models
from django_pandas.io import read_frame
from collections import defaultdict
from json import dumps
from django.urls import reverse

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
###########################################

class AppleTest(models.Model):
    investor = models.CharField(max_length=100, blank=True, primary_key = True)
    shares = models.CharField(max_length=10, blank=True, null=True)
    form_date = models.CharField(max_length=20, blank=True, null=True)

    @classmethod
    def return_df(self):

        obj = AppleTest.objects.all()

        df = read_frame(obj)

        return df

    @classmethod
    def return_json(self):

        df = self.return_df()

        js = df.to_json()

        return js

    @classmethod
    def graph(self):

        label_in_js = 'name'

        obj = AppleTest.objects.all().values()

        cik = defaultdict(dict)

        arr = []

        for d in obj:

            for inner in d:

                if inner == 'investor':

                    if d['form_date'] in ['19990630', '19991231']:

                        cik[d[inner]][d['form_date']] = int(float(d['shares']))

        for j in cik:



            if len(cik[j]) > 1:

                cik[j][label_in_js] = j
                arr.append(cik[j])


        return dumps(arr)




    class Meta:
        managed = False
        db_table = 'apple_test'

class MicroTest(models.Model):
    investor = models.CharField(max_length=100, blank=True, primary_key = True)
    shares = models.CharField(max_length=10, blank=True, null=True)
    form_date = models.CharField(max_length=20, blank=True, null=True)

    @classmethod
    def return_df(self):

        obj = MicroTest.objects.all()

        df = read_frame(obj)

        return df

    @classmethod
    def return_json(self):

        df = self.return_df()

        js = df.to_json()

        return js

    @classmethod
    def graph(self):

        label_in_js = 'name'

        obj = MicroTest.objects.all().values()

        cik = defaultdict(dict)

        arr = []

        for d in obj:

            for inner in d:

                if inner == 'investor':

                    if d['form_date'] in ['19990630', '19991231']:

                        cik[d[inner]][d['form_date']] = int(float(d['shares']))

        for j in cik:



            if len(cik[j]) > 1:

                cik[j][label_in_js] = j
                arr.append(cik[j])


        return dumps(arr)




    class Meta:
        managed = False
        db_table = 'micro_test'


class BeaCommodity(models.Model):
    commodity_code = models.CharField(max_length=10, blank=True, null=True)
    commodity = models.CharField(max_length=50, blank=True, null=True)
    id = models.AutoField(primary_key=True)


    def __str__(self):
        return f'Name:{self.commodity} - Commodity Code:{self.commodity_code}'

    class Meta:
        managed = False
        db_table = 'bea_commodity'


class BeaIndustry(models.Model):
    industry_code = models.CharField(max_length=20, blank=True, null=True)
    industry = models.CharField(max_length=50, blank=True, null=True)
    id = models.AutoField(primary_key=True)

    def get_absolute_url(self):

        return reverse('industry_single', args=[str(self.id)])

    def __str__(self):
        return f'Name:{self.industry} - Industry Code:{self.industry_code}'

    class Meta:
        managed = False
        db_table = 'bea_industry'

class Cik(models.Model):

    id = models.BigAutoField(primary_key=True)
    short_cik = models.CharField(max_length=15, blank=True, null=True)
    investor = models.CharField(max_length=500, blank=True, null=True)
    long_cik = models.CharField(max_length=15, blank=True, null=True)
    ticker = models.CharField(max_length=12, blank=True, null=True)
    investors = models.BigIntegerField()

    def __str__(self):

        return f"Cik Name:{self.investor} - Long Cik:{self.long_cik}"

    def get_absolute_url(self):

        return reverse('cik_single', args=[str(self.id)])

    def get_investor_url(self):

        return reverse('form_entries', args=[str(self.id)])

    class Meta:
        managed = False
        db_table = 'cik'

class Cusip(models.Model):

    id = models.BigAutoField(primary_key=True)

    short_cusip = models.CharField(max_length=7, blank=True, null=True)
    cusip = models.CharField(max_length=10, blank=True, null=True)
    desc_cusip = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):

        return f"Cusip Number:{self.cusip} - Desc - {self.desc_cusip}"

    def get_absolute_url(self):

        pass

    class Meta:
        managed = False
        db_table = 'cusip'


class CikCusip(models.Model):
    id = models.BigAutoField(primary_key=True)
    cik_id = models.ForeignKey('Cik', db_column='cik_id', on_delete=models.DO_NOTHING, db_index=False, related_name='Cik.id')
    cusip_id = models.ForeignKey('Cusip', db_column='cusip_id', on_delete=models.DO_NOTHING, db_index=False, related_name = "Cusip.id")
    name = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):

        return f"{self.cik_id} - {self.cusip_id} -Cusip Name {self.name}"

    def get_absolute_url(self):
        pass
        #return reverse('landing', args=[str(self.id)])

    class Meta:
        managed = False
        db_table = 'cik_cusip'

class Dates(models.Model):

    id = models.BigAutoField(primary_key=True)
    form_date = models.CharField(max_length=20, blank=True, null=True)
    year = models.CharField(max_length=5, blank=True, null=True)
    day = models.CharField(max_length=5, blank=True, null=True)
    month = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):

        return f"Date:{self.form_date}"

    def get_absolute_url(self):
        pass

    class Meta:
        managed = False
        db_table = 'dates'

class FileType(models.Model):

    id = models.BigAutoField(primary_key=True)
    file_type = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):

        return f"File Type:{self.file_type}"

    def get_absolute_url(self):
        pass

    class Meta:
        managed = False
        db_table = 'file_type'

class Form(models.Model):

    id = models.BigAutoField(db_column='id', primary_key=True)
    shares = models.CharField(max_length=50, blank=True, null=True)

    cik_id = models.ForeignKey('Cik', db_column='cik_id', on_delete=models.DO_NOTHING, db_index=True, related_name='Cik.id+')
    cusip = models.ForeignKey('Cusip', db_column='cusip_id', on_delete=models.DO_NOTHING, db_index=False, related_name = "Cusip.id+")
    #report_date_id = models.ForeignKey('Dates', db_column='report_date_id', on_delete=models.DO_NOTHING, db_index=True, related_name='Dates.id+')
    #file_date_id =models.ForeignKey('Dates', db_column='file_date_id', on_delete=models.DO_NOTHING, db_index=True, related_name='Dates.id+')
    #file_type_id = models.ForeignKey('FileType', db_column='file_type_id', on_delete=models.DO_NOTHING, db_index=True, related_name='FileType.id+')

    def __str__(self):

        return f"SHARES: {self.shares} - CUSIP {self.cusip} - CIK {self.cik_id}"

    def get_absolute_url(self):
        pass


    class Meta:
        managed = False
        db_table = 'form'

class IndustryValues(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.CharField(max_length=20, blank=True, null=True)
    commodity_id = models.ForeignKey('BeaCommodity', db_column="commodity_id", on_delete=models.DO_NOTHING, db_index=False, related_name = "BeaCommodity.id+")
    industry_id = models.ForeignKey('BeaIndustry', db_column="industry_id", on_delete=models.DO_NOTHING, db_index=False, related_name = "BeaIndustry.id+")

    def __str__(self):

        return f"Commodity Key:{self.commodity_id} - Industry Key: {self.industry_id}"

    def get_absolute_url(self):
        pass


    class Meta:
        managed = False
        db_table = 'industry_values'


class NumTest(models.Model):

    value = models.CharField(max_length=100, blank=True, null=True)
    tag = models.CharField(max_length=257, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, primary_key=True)

    @classmethod
    def table(self):

        b = NumTest.objects.all()

        b = read_frame(b)

        b = b.drop_duplicates(subset=['name','tag'], keep='last')

        b = b.pivot(index='name',columns='tag', values='value')

        headers = list(b.columns)

        values = b.T.to_dict(orient='list')

        return {'headers':headers, 'values':values}



    class Meta:
        managed = False
        db_table = 'num_test'

class SicNaics(models.Model):
    id = models.BigAutoField(primary_key=True)
    sic = models.CharField(max_length=10, blank=True, null=True)
    sic_desc = models.CharField(max_length=100, blank=True, null=True)
    naics = models.CharField(max_length=20, blank=True, null=True)
    naics_desc = models.CharField(max_length=200, blank=True, null=True)
    sec_code = models.CharField(max_length=5, blank=True, null=True)
    sec_desc = models.CharField(max_length=150, blank=True, null=True)
    sec_sub_desc = models.CharField(max_length=150, blank=True, null=True)


    def get_absolute_url(self):
        pass


    def __str__(self):
        return f'SIC:{self.sic_desc} - NAICS:{self.naics_desc} - SEC:{self.sec_sub_desc}'


    @classmethod
    def return_df(self):

        obj = SicNaics.objects.all()

        df = read_frame(obj)

        return df

    @classmethod
    def return_json(self):

        df = self.return_df()

        js = df.to_json()

        return js


    class Meta:
        managed = False
        db_table = 'sic_naics'

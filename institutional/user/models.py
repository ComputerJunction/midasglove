from distutils.sysconfig import customize_compiler
from django.db import models
from django.db import connection
from django_pandas.io import read_frame

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


class PCikAndCusip(models.Model):
    report_date = models.CharField(max_length=25, blank=True, null=True)
    cik = models.CharField(max_length=120, blank=True, null=False, primary_key=True)
    cusip = models.CharField(max_length=10, blank=True, null=True)
    year = models.CharField(max_length=6, blank=True, null=True)
    cusip6 = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_cik_and_cusip'

    def return_json():

        context = PCikAndCusip.objects.all()
        
        context = read_frame(context)

        context = context.to_json()

        return context
       


class PCikTicker(models.Model):
    cik = models.CharField(max_length=20, blank=True, null=False, primary_key=True)
    ticker = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_cik_ticker'


class PCikToCusip(models.Model):
    cik = models.CharField(max_length=120, blank=True, null=False, primary_key=True)
    cusip = models.CharField(max_length=10, blank=True, null=True)
    year = models.CharField(max_length=6, blank=True, null=True)
    cusip6 = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_cik_to_cusip'


class PCikmap(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    report_date = models.CharField(max_length=25, blank=True, null=True)
    cik = models.CharField(max_length=15, blank=True, null=False, primary_key=True)

    
    class Meta:
        managed = False
        db_table = 'p_cikmap'


class PComByInd(models.Model):
    commodity = models.CharField(max_length=200, blank=True, null=False, primary_key=True)
    industry = models.CharField(max_length=200, blank=True, null=True)
    value = models.CharField(max_length=20, blank=True, null=True)
    commodity_code = models.CharField(max_length=100, blank=True, null=True)
    industry_code = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_com_by_ind'


class PForm13F(models.Model):
    cik = models.CharField(max_length=50, blank=True, null=False, primary_key=True)
    cusip = models.CharField(max_length=50, blank=True, null=True)
    shares = models.CharField(max_length=50, blank=True, null=True)
    report_date = models.CharField(max_length=50, blank=True, null=True)
    file_date = models.CharField(max_length=50, blank=True, null=True)
    file_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_form13f'


class PSicToNaics(models.Model):
    sic = models.CharField(max_length=10, blank=True, null=False, primary_key=True)
    sic_desc = models.CharField(max_length=200, blank=True, null=True)
    naics = models.CharField(max_length=20, blank=True, null=True)
    naics_desc = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_sic_to_naics'

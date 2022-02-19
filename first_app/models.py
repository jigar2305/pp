from django.db import models

# Create your models here.
class role(models.Model):
    roleid = models.AutoField(primary_key=True)
    rolename = models.CharField(max_length=50)
    class meta:
        db_table = "role"

class users(models.Model):
    userid  = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    roleid = models.ForeignKey(role, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20)
    on_joinnig = models.DateTimeField(auto_now_add=True)
    on_resign = models.DateTimeField(auto_now_add=True)

    class meta:
        db_table = 'users'

class project(models.Model):
    projectid  = models.AutoField(primary_key=True)
    projectname = models.CharField(max_length=50)
    companyname = models.CharField(max_length=50)
    projectstatus = models.CharField(max_length=50)

    class meta:
        db_table = 'project'

class bugdetail(models.Model):
    budid = models.AutoField(primary_key=True)
    bug_decs = models.CharField(max_length=50)
    on_create = models.DateTimeField(auto_now_add=True)
    on_update = models.DateTimeField(auto_now_add=True)
    bugstatus = models.CharField(max_length=50)
    bugtype = models.CharField(max_length=50)

    class meta:
        db_table ='bugdetail'

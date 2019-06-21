from django.db import models


# Create your models here.
class Organization(models.Model):
    org_name = models.CharField(max_length=100)
    org_sub_name = models.CharField(max_length=100, blank=True)
    org_crn = models.CharField(max_length=10, blank=True, unique=True)
    org_header = models.CharField(max_length=20, blank=True)
    org_address = models.CharField(max_length=200, blank=True)
    org_tel_num = models.CharField(max_length=50, blank=True)
    org_desc = models.CharField(max_length=200, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'organization'

    def __str__(self):
        return self.org_name

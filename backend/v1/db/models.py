from django.db import models
from django_mysql.models import JSONField
from django.core.validators import MinLengthValidator


class LandingPageDB(models.Model):
    landing_id = models.CharField(max_length=24, validators=[MinLengthValidator(24)])
    data = JSONField()
    schema = JSONField()
    user_agent = models.CharField(blank=True, max_length=256)
    ip_v4_address = models.CharField(blank=True, max_length=19, validators=[MinLengthValidator(19)])
    registered_date = models.DateTimeField()

    class Meta:
        db_table = 'landing_page_db'

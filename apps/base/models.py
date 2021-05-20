from django.db import models
from django.utils.translation import gettext as _

# Create your models here
class BaseModel(models.Model):
    """
    Base model used for each model in the application
    """    
    id = models.AutoField(primary_key=True)
    state = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    deleted_date = models.DateField(auto_now=True)

    class Meta:
        # no tiene str
        abstract = True
        verbose_name = _("BaseModel")
        verbose_name_plural = _("BaseModels")

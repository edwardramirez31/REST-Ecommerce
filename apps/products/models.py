from django.db import models
from django.db.models.base import ModelStateFieldsCacheDescriptor
from django.urls import reverse
from django.utils.translation import gettext as _
from apps.base.models import BaseModel
from simple_history.models import HistoricalRecords

# Create your models here.
class MeasureUnit(BaseModel):
    """
    Measure unit from a product
    """
    
    description = models.CharField(max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = _("MeasureUnit")
        verbose_name_plural = _("MeasureUnits")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("MeasureUnit_detail", kwargs={"pk": self.pk})


class CategoryProduct(BaseModel):

    description = models.CharField(
        max_length=50, blank=False, null=False, unique=True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name=_("Product Measure Unit"))
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})


class Indicator(BaseModel):

    discount_value = models.PositiveSmallIntegerField(default=0)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name=_("Category Product Indicator"))
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = _("Indicator")
        verbose_name_plural = _("Indicators")

    def __str__(self):
        return f"{self.discount_value} from {self.category_product}"

    def get_absolute_url(self):
        return reverse("Indicator_detail", kwargs={"pk": self.pk})


class Product(BaseModel):

    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(_("Product Description"), blank=False, null=False)
    image = models.ImageField(_("Product Image"), upload_to='products/', blank=True, null=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"pk": self.pk})


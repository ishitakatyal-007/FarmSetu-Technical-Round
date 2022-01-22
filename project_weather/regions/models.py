from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.
class RegionModel(TimeStampedModel):
    region_id = models.AutoField(
        primary_key=True,
        help_text='Unique ID for region',
        verbose_name='Region ID'
    )
    region_name = models.CharField(
        max_length=100,
        help_text='Name of Region',
        verbose_name='Region Name'
    )

    def __str__(self) -> str:
        return self.region_name

    class Meta:
        db_table = 'regions'
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'
        ordering = ('created', )

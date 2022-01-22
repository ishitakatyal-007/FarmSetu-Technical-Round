from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.
from regions.models import RegionModel
from categories.models import CategoryModel

class YearlyStatisticsModel(TimeStampedModel):
    statistics_id = models.AutoField(
        primary_key=True,
        help_text='Unique ID for statistics',
        verbose_name='Statistic ID'
    )
    year = models.IntegerField(
        help_text='Year for statistics',
        verbose_name='Year'
    )
    region = models.ForeignKey(
        RegionModel,
        on_delete=models.PROTECT,
        help_text='Region',
        verbose_name='Region'        
    )
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.PROTECT,
        help_text='Category',
        verbose_name='Category'        
    )
    highlight_stats = models.FloatField(
        default=-1,
        help_text='Statistics',
        verbose_name='Statistics'
    )

    def __str__(self):
        return self.statistics_id

    class Meta:
        db_table = 'prev_year_statistics'
        verbose_name = 'Previous Year Statistic'
        verbose_name_plural = 'Previous Year Statistics'
        ordering = ('year', 'region', 'category',)
from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.
class CriterionModel(TimeStampedModel):
    criterion_id = models.AutoField(
        primary_key=True,
        help_text='Unique ID for criterion',
        verbose_name='Criterion ID'
    )
    criterion_name = models.CharField(
        max_length=100,
        help_text='Name of Criterion',
        verbose_name='Criterion Name'
    )

    def __str__(self) -> str:
        return self.criterion_name.capitalize()

    class Meta:
        db_table = 'criteria'
        verbose_name = 'Criteria'
        verbose_name_plural = 'Criterion'
        ordering = ('criterion_name', )

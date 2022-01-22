from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.
class CategoryModel(TimeStampedModel):
    category_id = models.AutoField(
        primary_key=True,
        help_text='Unique ID for category',
        verbose_name='Category ID'
    )
    category_name = models.CharField(
        max_length=100,
        help_text='Name of Category',
        verbose_name='Category Name'
    )
    category_alias = models.CharField(
        default='',
        max_length=50,
        help_text='Category Alias',
        verbose_name='Category Alias'
    )

    def __str__(self) -> str:
        return self.category_name

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('category_name', )

from django.db import models

# Create your models here.


class PhysicalTree(models.model):
    branch_count = models.IntegerField()
    bark_thickness_mm = models.DecimalField(max_length=7, decimal_places=4)
    tree_type = models.CharField(max_length=256)


class TreeRoot(models.model):
    PhysicalTree = models.ForeignKey(PhysicalTree, related_name='roots')
    root_thickness_mm = models.DecimalField(max_length=7, decimal_places=4)
    root_length_cm = models.DecimalField(max_length=12, decimal_places=4)
    root_type = models.CharField(max_length=256)


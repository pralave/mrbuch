from django.db import models
from oscar.apps.catalogue.abstract_models import AbstractProduct
from multiselectfield import MultiSelectField

REGION_CHOICES = (
    ('Gujarat','Gujarat'),
    ('Pune','Pune'),
    ('Rajasthan','Rajasthan'),
)
BRANCH_CHOICES = (
    ('Mechanical','Mechanical'),
    ('BioMedical','BioMedical'),
    ('Computer', 'Computer'),
    ('Civil','Civil'),
    ('Electronics','Electronics'),
)

YEAR_CHOICES = (
    ('1 year','1 year'),
    ('2 year', '2 year'),
    ('3 year', '3 year'),
    ('4 year','4 year'),
    ('Post Graduation', 'Post Graduate'),
)

EXAM_CHOICES = (
    ('GATE','GATE'),
    ('CAT/MAT','CAT/MAT'),
    ('GRE','GRE'),
    ('GMAT','GMAT')
)

TECHNOLOGY_CHOICES = (
    ('Programming languages','Programming languages'),
    ('Electronics','Electronics'),
    ('Computer','Computer'),

)
class Product(AbstractProduct):
    region = models.CharField(max_length=60,choices=REGION_CHOICES, default='Pune', verbose_name='University Region',null=True)
    year = models.CharField(max_length=60,choices=YEAR_CHOICES, verbose_name='Year',null=True)
    branch = MultiSelectField(choices=BRANCH_CHOICES, verbose_name='Branch',null=True)
    exam = MultiSelectField(choices=EXAM_CHOICES, verbose_name='Exams',null=True)
    technology = MultiSelectField(choices=TECHNOLOGY_CHOICES, verbose_name='Technology',null=True)

from oscar.apps.catalogue.models import *
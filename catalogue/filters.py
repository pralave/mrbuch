import django_filters
from django import forms
from .models import Product

Region_Choices = (
    ('Gujarat','Gujarat'),
    ('Pune','Pune'),
    ('Rajasthan','Rajasthan'),
)
Branch_Choices = (
    ('Mechanical','Mechanical'),
    ('BioMedical','BioMedical'),
    ('Computer', 'Computer'),
    ('Civil','Civil'),
    ('Electronics','Electronics'),
)

Year_Choices = (
    ('1 year','1 year'),
    ('2 year', '2 year'),
    ('3 year', '3 year'),
    ('4 year','4 year'),
    ('Post Graduation', 'Post Graduate'),
)

Technology_Choices = (
    ('Programming Languages','Programming Languages'),
    ('Electronics', 'Electronics'),
    ('Java', 'Java'),
    ('C','C'),
    ('Data Structures', 'Data Structures'),
)


class ProductEngineeringFilter(django_filters.FilterSet):
    region = django_filters.ChoiceFilter(choices=Region_Choices, widget=forms.RadioSelect)
    year = django_filters.MultipleChoiceFilter(choices=Year_Choices, widget=forms.CheckboxSelectMultiple)
    branch = django_filters.MultipleChoiceFilter(choices=Branch_Choices, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Product
        fields = ['region','year', 'branch']

class ProductTechnologyFilter(django_filters.FilterSet):
    technology = django_filters.MultipleChoiceFilter(choices=Technology_Choices, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Product
        fields = ['technology',]
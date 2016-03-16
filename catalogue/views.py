from django.contrib import messages
from django.shortcuts import redirect
from django.core.paginator import InvalidPage
from django.utils.translation import ugettext_lazy as _

from oscar.apps.catalogue.views import ProductCategoryView as CoreProductCategoryView

from .filters import ProductEngineeringFilter, ProductTechnologyFilter
from .models import Product






class ProductCategoryView(CoreProductCategoryView):

    def get(self, request, *args, **kwargs):
        # Fetch the category; return 404 or redirect as needed
        self.product_engineering_filter = ProductEngineeringFilter(request.GET, queryset=Product.objects.all())
        self.product_technology_filter = ProductTechnologyFilter(request.GET, queryset=Product.objects.all())
        self.category = self.get_category()
        potential_redirect = self.redirect_if_necessary(
            request.path, self.category)
        if potential_redirect is not None:
            return potential_redirect

        try:
            self.search_handler = self.get_search_handler(
                request.GET, request.get_full_path(), self.get_categories())
        except InvalidPage:
            messages.error(request, _('The given page number was invalid.'))
            return redirect(self.category.get_absolute_url())

        return super(ProductCategoryView, self).get(request, *args, **kwargs)



    def get_context_data(self, **kwargs):
        context = super(ProductCategoryView, self).get_context_data(**kwargs)
        context['category'] = self.category
        search_context = self.search_handler.get_search_context_data(
            self.context_object_name)
        product_engineering_filters = self.product_engineering_filter
        product_technology_filters = self.product_technology_filter
        context['product_engineering_filter'] = product_engineering_filters
        context['product_technology_filter'] = product_technology_filters
        context['product_category'] = self.category

        context.update(search_context)
        return context
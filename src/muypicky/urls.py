"""muypicky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

# from restaurants.views import *
from rrestaurants.views import *

from kotrana001.views import *
from kotrana002.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello_world/', hello_world),
    url(r'^home_with_var_passed/', home_with_var_passed),

    url(r'^home/', home1),
    url(r'^about/', about),

    url(r'^contact_class_view/', ContactView.as_view()),
    url(r'^contact_class_templateview/', ContactTemplateView.as_view()),
    url(r'contact_template_view_immediately', TemplateView.as_view(
        template_name = 'contact.html'
        # # do not know why the line below does NOT work
        # , context = {
        #     'html_var': 'html_var002'
        #     , 'num': 88
        #     , 'some_list': [5, 6, 7, 8]
        # }
    )),
    url(r'^restaurants_list/', restaurants_list),
    url(r'^restaurants/add/', add_rrestaurant),
    url(r'^restaurants_list/(?P<slug>\w+)', SearchCatListView.as_view()),
    url(r'^add_restau_short_template/', add_restau_short_template), 
    url(r'^add_restau_uses_modelform/', add_restau_uses_modelform),

    url(r'^kotrana001/aff_base', kotrana001_aff_base),
    url(r'^kotrana001/kotrana001_add_form001', kotrana001_add_form001),
    url(r'^kotrana001/all_model001', kotrana001_all_model001),
    url(r'^kotrana001/kotrana001_modelform001_add', kotrana001_modelform001_add),

    url(r'^kotrana001/all_model002', kotrana001_all_model002),
    url(r'kotrana001/add_model002', kotrana001_add_model002),    
    url(r'^kotrana001/from_form_add_model002', add_model002_from_form),    
    # url(r'^kotrana001/create_model002', kotrana001_create_model002),
    # url(r'^kotrana001/kotrana001_modelform001', kotrana001_modelform001),    



    url(r'^kotrana002/test001', kotrana002_test001),  
    url(r'^kotrana002/acceuil', kotrana002_acceuil),  
    url(r'^kotrana002/presentation', kotrana002_presentation),  
    url(r'^kotrana002/actualite', kotrana002_actualite),  
    url(r'^kotrana002/portfolio', kotrana002_portfolio),  
    url(r'^kotrana002/contact', kotrana002_contact),
    url(r'^kotrana002/single_folio', kotrana002_single_folio),

]
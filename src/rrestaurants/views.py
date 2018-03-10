from django.shortcuts import render
from django.http import (
    HttpResponse
    , HttpResponseRedirect
)
import random
from django.views import View
from django.views.generic import (
    TemplateView    # this is useful, when 
    , ListView      # this is useful, when we want to filter something in our database
)

from .forms import RRestaurantForm, RRestaurantModelForm

from .models import RRestaurants, RRestaurantsLocation

def add_restau_uses_modelform(request):
    form001 = RRestaurantModelForm(
        request.POST or 
        None
    )   # that class(RRestaurantForm) is going to set the thing which we want to see in 
        # # in the form.html

    if form001.is_valid(): # first of all, this is going to happen if request.POST is OK

        form001.save()  # this line is VERY VERY IMPORTANT
                        # # it is going to take all of the vars which came from the request(template_html)
                        # # and going to save into the database IMMEDIATELY

        return HttpResponseRedirect('/restaurants_list/')   # you should know this, 
                                        # # going to redirect to that url001, that url001 is going to redirect some method or class in views.py

    errors = None
    if form001.errors:  # this is going to be raised when you decided to raise it
                        # # this is going to be raised by def__clean_location@class__RRestaurantForm@src/rrestaurants/views.py
        errors = form001.errors
        pass

    context = { # remember, we are going to come here when there is NO request.POST
        'form001' : form001
        , 'errors': errors  # remember, this is going to get value when there is error(which we defined just above) ONLY
                            # # it is better that you do NOT print this {{ errors }} into template_html
    }
    return render(
        request
        , 'rrestaurants/rrestaurantslocation_add_shortened.html'
        , context
    )


def add_restau_short_template(request):
    form001 = RRestaurantForm(
        request.POST or 
        None
    )   # that class(RRestaurantForm) is going to set the thing which we want to see in 
        # # in the form.html

    if form001.is_valid(): # first of all, this is going to happen if request.POST is OK
        RRestaurantsLocation.objects.create(        # you should know this already
            name = form001.cleaned_data.get('name') # # this is going to insert into db
            , location = form001.cleaned_data.get('location')
            , category = form001.cleaned_data.get('category')
        )
        return HttpResponseRedirect('/restaurants_list/')   # you should know this, 
                                        # # going to redirect to that url001, that url001 is going to redirect some method or class in views.py

    errors = None
    if form001.errors:  # this is going to be raised when you decided to raise it
                        # # this is going to be raised by def__clean_location@class__RRestaurantForm@src/rrestaurants/views.py
        errors = form001.errors
        pass

    context = { # remember, we are going to come here when there is NO request.POST
        'form001' : form001
        , 'errors': errors  # remember, this is going to get value when there is error(which we defined just above) ONLY
                            # # it is better that you do NOT print this {{ errors }} into template_html
    }
    return render(
        request
        , 'rrestaurants/rrestaurantslocation_add_shortened.html'
        , context
    )

    pass

def add_rrestaurant(request):
    context = {}
    if (request.POST):

        # print('len(request.POST): ', len(request.POST))
        # print('request.POST: ', request.POST)
        # # notice, if you set void to all of the form.html... you are going to get something similar to this in request.POST
        # # # {'name': '', 'location': '', ...}
        
        RRestaurantsLocation.objects.create(
            name = request.POST.get('name')
            , location = request.POST.get('location')   # it is not good to have this style, better let django clean the data first
                                                        # # at that time, you should use forms.py
            , category = request.POST.get('category')
        )
        return HttpResponseRedirect('/restaurants_list/')
    else:
        template_name = 'rrestaurants/rrestaurantslocation_add.html'
        print('Request.POST of ""add_rrestaurant"" is void')
        return render(
            request
            , template_name
        )
        pass
   
    

# Create your views here.
# Create your views here.
def hello_world(request):   # remember, this view is going to get the request and it is going to return some html
    return HttpResponse('Hello World')   # html_response of the server... this html_response is going to be from "from django.shortcuts import render"
    # normally, this is something like:
    # return render(request, template001, dict_of_data001)

def about(request):
    return render(
        request
        , 'about.html'
    )
    pass

def contact(request):
    return render(
        request
        , 'contact.html'
    )
    pass

def home1(request):
    return render(
        request
        , 'home1.html'
    )
    pass

def home_with_var_passed(request):
    random_num = random.randint(0, 23456787654)
    list_random_num = [
        random.randint(0, 23456787654)
        , random.randint(0, 23456787654)
        , random.randint(0, 23456787654)
        , random.randint(0, 23456787654)
    ]
    return render(
        request 
        , 'study001.html'
        , {
            'random_num': random_num
            , 'html_var': 'html_var001'
            , 'list_random_num': list_random_num
        }
    )


class ContactView(View):
    def get(self,request, *args, **kwargs):
        context = {}
        return render(request, "contact.html", context)
        pass

class ContactTemplateView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, *args, **kwargs):
        super(
            ContactTemplateView
            , self
        ).get_context_data(
            *args
            , **kwargs
        )   # afaik, this is mandatory in TemplateView001


        context = {
            'html_var': 'html_var001'
            , 'num': 5
            , 'some_list': [
                random.randint(0, 23456787654)
                , random.randint(0, 23456787654)
                , random.randint(0, 23456787654)
            ]
        }
        return context

def restaurants_list(request):
    queryset = RRestaurantsLocation.objects.all()
    print('queryset: ', queryset)
    # for q in queryset:
    #     print('q.name: ', q.name)
    #     print('q.location: ', q.location)
    #     print('q.category: ', q.category)
    #     print('q.timestamp: ', q.timestamp)
    #     print('q.updated: ', q.updated)
    #     print('q.date_field001: ', q.date_field001) 
    context = {
        'object_list': queryset
    }
    return render(
        request
        , 'rrestaurants/rrestaurant_list.html'
        , context
    )
    pass

class SearchCatListView(ListView):
    template_name = 'rrestaurants/rrestaurant_list.html'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        print('slug:', slug)
        if slug:
            print ('niditra ato')
            queryset = RRestaurantsLocation.objects.filter( category = slug )
        else:
            queryset = RRestaurantsLocation.objects.none()
        return queryset
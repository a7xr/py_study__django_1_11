from django.shortcuts import render

from .models import *

from .forms import *

from django.http import (
    HttpResponse
    , HttpResponseRedirect
)


def add_model002_from_form(request):
    form001 = Model002_Form(
        request.POST or 
        None
    )   # that class(Model002_Form) is going to set the thing which we want to see in 
        # # in the form.html

    if form001.is_valid(): # first of all, this is going to happen if request.POST is OK
        Kotrana001_Model002.objects.create(        # you should know this already
            name = form001.cleaned_data.get('name') # # this is going to insert into db
            , location = form001.cleaned_data.get('location')
        )
        return HttpResponseRedirect('/restaurants_list/')   # you should know this, 
                                        # # going to redirect to that url001, that url001 is going to redirect some method or class in views.py

    errors = None
    if form001.errors:  # this is going to be raised when you decided to raise it
                        # # this is going to be raised by def__clean_location@class__Model002_Form@src/rrestaurants/views.py
        errors = form001.errors
        pass

    context = { # remember, we are going to come here when there is NO request.POST
        'form001' : form001
        , 'errors': errors  # remember, this is going to get value when there is error(which we defined just above) ONLY
                            # # it is better that you do NOT print this {{ errors }} into template_html
    }
    return render(
        request
        , 'kotrana001/kotrana001_add_model002.html'
        , context
    )

def kotrana001_add_model002(request):
    if (request.POST):

        Kotrana001_Model002.objects.create(
            first_name = request.POST.get('first_name')
            , last_name = request.POST.get('last_name')   # it is not good to have this style, better let django clean the data first
                                                        # # at that time, you should use forms.py
        )

        # return HttpResponse('FirstName you inserted was: ' + str(request.POST.get('first_name')))
        return HttpResponseRedirect('/kotrana001/all_model002')
        pass
    else:
        return render(
            request
            , 'kotrana001/kotrana001_add_model002.html'
            , {}
        )
        pass
    pass

def kotrana001_all_model002(request):
    if (request.POST):
        # normalement, tsy mandalo ato mitsn
        pass
    else:
        queryset = Kotrana001_Model002.objects.all()
        context = {
            'object_list': queryset
        }
        return render(
            request
            , 'kotrana001/kotrana001_all_model002.html'
            , context
        )
        pass


def kotrana001_all_model001(request):
    if (request.POST):
        # normalement, tsy mandalo ato mitsn
        pass
    else:
        queryset = Kotrana001_Model001.objects.all()
        context = {
            'object_list': queryset
        }
        return render(
            request
            , 'kotrana001/kotrana001_all_model001.html'
            , context
        )
        pass

# Create your views here.
def kotrana001_aff_base(request):
    context = {}
    if(request.POST):
        # normalement tsy mandalo ato mitsn satri tsis button_form ao am html io ambany
        pass
    else:
        return render(
            request
            , 'kotrana001/kotrana001_base.html'
            , context
        )
    pass

def kotrana001_add_form001(request):
    context = {}
    if(request.POST):
        return HttpResponse('Name you inserted was: ' + str(request.POST.get('name')))
        pass
    else:
        return render(
            request
            , 'kotrana001/kotrana001_add_form001.html'
            , context
        )
    pass

def kotrana001_modelform001_add(request):
    form001 = Kotrana001_Model001_ModelForm( # once again, this extends from forms.ModelForm001
        request.POST or None
    )
    if form001.is_valid():
        form001.save()
        return HttpResponseRedirect('/kotrana001/kotrana001_modelform001_add/')
        pass
    errors = None

    if form001.errors:
        errors = form001.errors

    context = { 
        'form001': form001
        , 'errors': errors
    }

    return render(
        request
        , 'kotrana001/kotrana001_modelform001_add.html'
        , context
    )

    pass
from django.shortcuts import render

from .models import Kotrana001_Model001

from .forms import Kotrana001_Model001_Form

from django.http import (
    HttpResponse
    , HttpResponseRedirect
)

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

def kotrana001_form001(request):
    context = {}
    if(request.POST):
        return HttpResponse('Name you inserted was: ' + str(request.POST.get('name')))
        pass
    else:
        return render(
            request
            , 'kotrana001/kotrana001_form001.html'
            , context
        )
    pass

def kotrana001_modelform001(request):
    form001 = Kotrana001_Model001_Form(request.POST or None)
    if form001.is_valid():
        form001.save()
        return HttpResponseRedirect('/kotrana001/kotrana001_form001/')
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
        , 'kotrana001/kotrana001_modelform001.html'
        , context
    )

    pass
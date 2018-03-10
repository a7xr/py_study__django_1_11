from django.shortcuts import render

from django.http import (
    HttpResponse
    , HttpResponseRedirect
)

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
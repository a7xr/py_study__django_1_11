from django.shortcuts import render

# Create your views here.
from django.http import (
    HttpResponse
    , HttpResponseRedirect
)

def kotrana002_test001(request):
	return render(
		request
		, 'kotrana002/base002.html'
		, {}
	)
	pass

def kotrana002_acceuil(request):
	return render(
		request
		, 'kotrana002/acceuil002.html'
		, {}
	)
	pass





def kotrana002_presentation(request):
	return render(
		request
		, 'kotrana002/presentation002.html'
		, {}
	)
	pass

def kotrana002_actualite(request):
	return render(
		request
		, 'kotrana002/actualite002.html'
		, {}
	)
	pass

def kotrana002_portfolio(request):
	return render(
		request
		, 'kotrana002/portfolio002.html'
		, {}
	)
	pass

def kotrana002_contact(request):
	return render(
		request
		, 'kotrana002/contact002.html'
		, {}
	)
	pass



def kotrana002_single_folio(request):
	return render(
		request
		, 'kotrana002/single_folio002.html'
		, {}
	)
	pass
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):	# remember, this view is going to get the request and it is going to return some html
	return HttpResponse('Hello World')	 # html_response of the server... this html_response is going to be from "from django.shortcuts import render"
	# normally, this is something like:
	# return render(request, template001, dict_of_data001)



def home_with_var_passed(request):
	return render(
		request 
		, 'base.html'
		, {
			'html_var': 'html_var001'
		}
	)
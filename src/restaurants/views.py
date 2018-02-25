from django.shortcuts import render
from django.http import HttpResponse
import random
from django.views import View
from django.views.generic import TemplateView

# Create your views here.
def hello_world(request):	# remember, this view is going to get the request and it is going to return some html
	return HttpResponse('Hello World')	 # html_response of the server... this html_response is going to be from "from django.shortcuts import render"
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
		super(ContactTemplateView, self).get_context_data(*args, *kwargs)
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
	context = {
		'some_list': [1, 2, 3, 4, 5]
	}
	return render(
		request
		, 'restaurants/restaurant_list.html'
		, context
	)
	pass
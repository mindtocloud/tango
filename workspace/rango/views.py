from django.shortcuts import render
from django.http import HttpResponse

def index(request):

	# Construct a dictionary to pass to the the template engine as its context.

	context_dic = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}


	 # Return a rendered response to send to the client.
	 # We make use of the shortut funtion to make our lives easier
	 # Note that the first parameter is the template we wish to use.
	return render(request, 'rango/index.html', context=context_dic)

def about(request):
	context_dic = {'yourname': 'Nick'}
	return render(request, 'rango/about.html', context = context_dic)



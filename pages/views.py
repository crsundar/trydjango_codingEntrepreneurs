from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs):
	return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html")

def about_view(request, *args, **kwargs):
	my_context = {
		"my_text": "This is about us",
		"my_number": 123,
		"my_list": [123, 4242, 12323, "abc"]
	}
	return render(request, "about.html", my_context)
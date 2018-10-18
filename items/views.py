from django.shortcuts import render

from .models import Item

def item_detail_view(request):
	obj = Item.objects.get(id=1)
	context = {
		'title': obj.title,
		'description': obj.description
	}
	return render(request, "item/detail.html", context)
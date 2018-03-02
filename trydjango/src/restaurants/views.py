from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .forms import RestaurantCreateForm
from .models import RestaurantLocation

def restaurant_createview(request):
	# print(request.GET)

	if request.method == "POST":
		form = RestaurantCreateForm(request.POST)
		if form.is_valid():
			obj = RestaurantLocation.objects.create(
					name = form.cleaned_data.get('name'),
					location = form.cleaned_data.get('location'),
					category = form.cleaned_data.get('category'),					
				)
			return HttpResponseRedirect("/restaurants/")
		if form.errors:
			print(form.errors)
	template_name = 'restaurants/form.html'
	context = {}
	return render(request, template_name, context)

def restaurant_listview(request):
	template_name = 'restaurants/restaurants_list.html'
	queryset = RestaurantLocation.objects.all()
	print(queryset)
	context = {
		"object_list": queryset
	}
	return render(request, template_name, context)

class RestaurantListView(ListView):
	def get_queryset(self):
		slug = self.kwargs.get("slug")
		if slug:
			queryset = RestaurantLocation.objects.filter(
				Q(category__iexact=slug) |
				Q(category__icontains=slug)
			)
		else:
			queryset = RestaurantLocation.objects.all()
		return queryset

class RestaurantDetailView(DetailView):
	queryset = RestaurantLocation.objects.all()
	# def get_object(self, *args, **kwargs):
	# 	rest_id = self.kwargs.get('rest_id')
	# 	obj = get_object_or_404(RestaurantLocation, id = rest_id) #pk = rest_id
	# 	return obj

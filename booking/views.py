from django.shortcuts import render
from django.views.generic import ListView
from shops.models import Shops
from django.db.models import Q # new

# Create your views here.

class ShopListView(ListView):
	model = Shops
	template_name = 'booking/search.html'
	context_object_name= 'Shops'

	def get_queryset(self): # new
	    query = self.request.GET.get('q')
	    #query1 = self.request.GET.GET('q1')
	    #query2 = self.request.GET.GET('q2')
	    object_list = Shops.objects.filter(
	        Q(city=query)
	    )
	    return object_list

#& Q(area=query1) & Q(typesport=query2) 
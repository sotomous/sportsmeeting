from django.shortcuts import render

# Create your views here.

def join(request):
	return render(request, 'shops/join.html')


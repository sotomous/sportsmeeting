from django.shortcuts import render

# Create your views here.



posts = [       								#gia na perasoume dedomena sthn selida dynamikos(gai thn wra)
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
	context = {						#create dictionary that willtake posts dictionary with the parakatw tropo
		'posts' : posts 			#'key':value  value=dictionary post

	}
	return render(request, 'homescreen/home.html', context) #it shows the home.html render(request,path html,emfanisi dedomenwn) 


def about(request):
    return render(request, 'homescreen/about.html', {'title':'about'})  #it shows the about.html render(request,path html)

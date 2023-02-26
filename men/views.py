from django.http import HttpResponse
from django.shortcuts import render

from men.models import Men

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]
def index(request):
    posts = Men.objects.all()
    return render(request, 'men/index.html', {'posts':posts, 'menu': menu, 'title': 'Home' })

def categories(request, categoryid):
    return HttpResponse(f"<h1>ksdjfjnhsdj</h1><p>{categoryid}</p>")

def about(request):
    return render(request, 'men/about.html', {'menu':menu, 'title': 'about'})

def error404(request):
    return render(request, 'men/404.html')

def error403(request):
    return render(request, 'men/403.html')

def error500(request):
    return render(request, 'men/500.html')

def error400(request):
    return render(request, 'men/400.html')
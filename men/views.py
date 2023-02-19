from django.http import HttpResponse
from django.shortcuts import render

from men.models import Men, Category, Post

menu = [{'title': "О сайте",'url_name': 'about'},
        {'title':"Добавиь статью", 'url_name': 'add_page'},
        {'title':"Обратная связь", 'url_name':'contact'},
        {'title' :"Войти", 'url_name': 'login'}]
def index(request):
    posts = Post.objects.all()
    cats = Category.objects.all
    context = {
        'posts': posts,
        'cats':cats,
        'menu':menu,
        'title':'Home',
        'cat_selected': 0,
    }
    return render(request, 'men/index.html',context=context)


def about(request):
    return render(request, 'men/about.html', {'menu':menu, 'title': 'about'})

def error404(request,exception):
    return render(request, 'men/404.html')

def error403(request):
    return render(request, 'men/403.html')

def error500(request):
    return render(request, 'men/500.html')

def error400(request):
    return render(request, 'men/400.html')

def product(request):
    posts = Post.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats' : cats,
        'menu': menu,
        'title': 'Home',
        'cat_selected': 0,
    }
    return render(request, 'men/product.html',context=context)


def show_post(request, post_id):
    return HttpResponse(f"id = {post_id}")

def show_category(request, cat_id):
   posts = Post.objects.filter(cat_id=cat_id)
   cats = Category.objects.all()

   context = {
       'posts' : posts,
        'cats': cats,
       'menu': menu,
       'title': 'Home',
       'cat_selected': cat_id,
   }
   return render(request, 'men/product.html', context=context)
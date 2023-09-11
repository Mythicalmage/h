from django.shortcuts import render
from models import Post


def index(request):
    t = Post.objects.all()

    return render(request, 'index.html', {'t': t})



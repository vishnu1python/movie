from django.shortcuts import render, HttpResponse, redirect
from .models import Movie
from .forms import MovieForm
from django.contrib import messages


def index(request):
    movie = Movie.objects.all()
    content = {
        'movielist': movie
    }

    return render(request, 'index.html', content)


def details(request, id):
    movie = Movie.objects.get(id=id)
    context = {
        'moviekey': movie
    }
    return render(request, 'details.html', context)


def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie = Movie(name=name, desc=desc, year=year, img=img)

        movie.save()
        return redirect('/')

    return render(request, 'add.html')


def update(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, "update.html", {'form': form, 'movie': movie})


def delete(request, id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, "delete.html")

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def index(request):
  if 'number' not in request.session:   
    request.session['number'] = 0
  word = get_random_string(length=14)
  request.session['number'] += 1
  return render(request, 'temp/index.html', {'word': word, 'number': request.session['number']})

def generate(request):
  return redirect('/random')

def resetWord(request): 
  request.session.clear()
  return redirect('/random')

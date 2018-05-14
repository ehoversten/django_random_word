from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count']= 0

    data = {

    }
    return render(request, 'random_word_gen/index.html', data)


def process(request):
    if request.method == 'POST':
        print("*"*50)
        print(request.POST)
        rando_word = get_random_string(length=14)
        print('Word:', rando_word)
        request.session['word'] = rando_word
        # print(request.session['word'])
        request.session['count']+=1
        print('Attempt #', request.session['count'])
        print("*"* 50)
        return redirect('/')
    else:
        return redirect('/')


def reset(request):
    request.session.clear()
    return redirect('/')

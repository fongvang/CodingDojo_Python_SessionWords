from django.shortcuts import render, redirect
from time import localtime, strftime
from . import models


# Create your views here.
def index(request):
    # if "word" not in request.session:
    #     request.session['word'] = ''   
    #     request.session['color'] = ''
    #     request.session['big_font'] = False
        # request.session['words'] = []
    if 'words' not in request.session:
        request.session['words']=[]
    return render(request, 'index.html')


def generate(request):
    words = request.POST['text'],
    color = request.POST['color'],
    showbig = request.POST['showbig']
        

    temp = request.session['words']
    temp.insert(0,{
        "words": words,
        "color": color,
        "showbig": showbig
    })

    request.session['words'] = temp

    return redirect('/')

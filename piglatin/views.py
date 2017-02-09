from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def translate(request):
    original = request.GET['originaltext'].lower()

    translation = ''
    for word in original.split():
        if word[0] in ["a", "e","i", "o", "u","y"]:
        # vowel
            translation += word
            translation += 'yay '
    else:
        #consonant
        # from second letter if first letter is not vowel,eg cheese
        translation += word[1:]
        # first consonant letter
        translation += word[0]
        # ay
        translation += 'ay'
    return render(request,'translate.html', {'original':original, 'translation': translation})

def about(request):
    return render(request,'about.html')

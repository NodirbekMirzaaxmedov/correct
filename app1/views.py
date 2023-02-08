from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def imlo(request):
    qidir = request.POST.get('searched')
    togri = Correct.objects.filter(word=qidir)
    notogri = []
    if len(togri)==0:
        notogri = Incorrect.objects.filter(word=qidir)
    else:
        notogri = Incorrect.objects.filter(correct=togri[0])
    data = {
        'togri': togri,
        'notogri':notogri,
    }

    return render(request,'result.html',data)
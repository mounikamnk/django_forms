from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def djform(request):
    SUFO=signupform()
    d={'SUFO':SUFO}
    if request.method=='POST':
        SUFDT=signupform(request.POST)
        if SUFDT.is_valid():
            n=SUFDT.cleaned_data['name']
            a=SUFDT.cleaned_data['age']
            m=SUFDT.cleaned_data['email']
            p=SUFDT.cleaned_data['pw']
            g=SUFDT.cleaned_data['gender']
            c=SUFDT.cleaned_data['courses']
        return HttpResponse(str(SUFDT.cleaned_data))
    return render(request,'djform.html',d)





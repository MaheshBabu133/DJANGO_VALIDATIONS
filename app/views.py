from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def Student(request):
    SF=StudentForm()
    d={'SF':SF}
    if request.method=='POST':
        FD=StudentForm(request.POST)
        if FD.is_valid():
            return HttpResponse(str(FD.cleaned_data))
            #cleaned data is a dictionary with Your submitted data)
    
    return render(request,'Student.html',d)
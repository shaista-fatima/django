from django.shortcuts import render,HttpResponse
from myapps.forms import StudentForm
# Create your views here.
def index(request):
    form=StudentForm(request.post)
    if request.method=='post':
        if form.is_valid():
            form.save()
            return HttpResponse("✔saved")
        else:
            return HttpResponse("error 🛑")
    else:
         return render(request,'index.html',{form:"form"})
    # return HttpResponse("hello world")

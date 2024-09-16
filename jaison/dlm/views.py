from django.shortcuts import render,redirect,get_object_or_404
from dlm.models import Student
from dlm.forms import StudentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def dlmadd(request):
    dlmform=StudentForm(request.POST or None)
    if dlmform.is_valid():
        dlmform.save()
        return redirect('viewdlm')
    return render(request,'dlmadd.html',{'form':dlmform})

@login_required
def viewdlm(request):
    alldlm=Student.objects.all()
    return render(request,'viewdlm.html',{'dlms':alldlm})

def editdlm(request,pk):
    dlm=get_object_or_404(Student,pk=pk)
    if request.method=='POST':
        dlmform=StudentForm(instance=dlm,data=request.POST)
        if dlmform.is_valid():
            dlmform.save()
            return redirect('viewdlm')

    else:
        dlmform = StudentForm(instance=dlm)
    return render(request,"dlmadd.html",{"form":dlmform,"object":viewdlm})


def deletedlm(request,pk):
    dlm=get_object_or_404(Student,pk=pk)
    if request.method=='POST':
        dlm.delete()
        return redirect('viewdlm')
    return render(request, 'deletedlm.html', {"dlm":dlm, "object":deletedlm})


from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from schoolapp.models import Attendence
from django.contrib import messages
# Create your views here.
def base(request):
    return render(request,'home.html')

def login(request):
    if request.method == 'POST':
        student_name = request.POST['studentName']
        roll_number = request.POST['rollNo']    

        if Attendence.objects.filter(name=student_name).exists():
            messages.info(request,"you are already logged in!")
            return redirect('/')


        else:
            data = Attendence(name=student_name)
            data.save()
            messages.success(request,'you are logged in now!')
            return redirect('/')



# def result(request):
#     if request.method =="POST":
#         studentName = request.POST['studentname']
#         if Attendence.objects.filter(name=studentName).exists():
#             messages.success(request,'you are logged in')
#             # detailsOfThatStudent = Attendence.objects.filter(name=studentName)
#             # context = {
#             #     'allDetails':detailsOfThatStudent
#             # }
#         else:
#             messages.info(request,'you was not log in')    

#         return render(request,'result.html')

def result(request):
    if request.method == 'POST':
        studentName = request.POST['studentname']
        studentRoll_number = request.POST['rollno']
        if Attendence.objects.filter(name=studentName,roll_number=studentRoll_number).exists():
            # messages.success(request,'you are logged in ')
            detailOfThatStudent = Attendence.objects.filter(name=studentName)
            print(detailOfThatStudent)
            context = {
                'allDetails':detailOfThatStudent
            }
            return render(request,'result.html',context)
        else:
            messages.info(request,'This Student detail is not in the school list,Check the details again!')    
    return render(request,'result.html')


def attendence(request):
     if request.method == 'POST':
        studentName = request.POST['studentname']
        studentRoll_number = request.POST['rollno']
        if Attendence.objects.filter(name=studentName,roll_number=studentRoll_number).exists():
            # messages.success(request,'you are logged in ')
            detailOfThatStudent = Attendence.objects.filter(name=studentName)
            print(detailOfThatStudent)
            context = {
                'allDetailsOfAttendence':detailOfThatStudent
            }
            return render(request,'attendence.html',context)
        else:
            messages.info(request,'This Student detail is not in the school list,Check the details again!')    
        return render(request,'attendence.html')    
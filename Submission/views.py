from django.http import HttpResponse
#from django.shortcuts import render


# def show_all(request):
#     return HttpResponse("All submission")
#
#
# def show_one(request):
#     return HttpResponse("Single submission")

from datetime import datetime
from xmlrpc.client import DateTime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
from Rooms.models import room
from Submission.models import Submission


def show_all(request, aid):
    if request.method == 'POST':
        user = request.user
        # assignment = Brands(id=1)
        assignment = room(id=aid)
        date = datetime.now()

        submit = Submission(user=user, assignment=assignment, date=date, )
        submit.save()
        # return HttpResponse('<script>alert("Room rented[ Check your booking] !")</script>')


    return render(request, 'Submission.html')

def show_my(request):
    #sub= Submission.object.all to import all

    # to import specific

    # sub= Submission.object.get(user=request.user)
    sub = Submission.objects.all()
    return render(request, 'mysubmission.html', {'subs':sub})


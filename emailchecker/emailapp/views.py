from django.shortcuts import render, redirect
from django.contrib import messages
import validate_email_address
from .forms import *


def index(request):
    emp = Emailform
    return render(request, "index.html", {"emp": emp})


def add(request):
    if request.method == "POST":
        emp = Emailform(request.POST)
        empval = emp['emal'].value()
        isExists = validate_email_address.validate_email(empval, verify=True)
        # isExists = True
        if isExists:
            print(isExists)
            return render(request, "index.html", {"exists": isExists})
        else:
            print(isExists)
            return render(request, "index.html", {"notexists": empval})

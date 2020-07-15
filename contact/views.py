from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm


def contact(request):

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('<script>alert("Your Quires are Successfully sent !")</script>')

    else:
        form = ContactForm()

        return render(request, "contact.html", {'form': form})


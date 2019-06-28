from django.shortcuts import render, redirect
from django import forms

# Create your views here.
from .models import QR2019

# class Lobqr19DetailView():
#forms as classes

class QR2019Form(forms.Form):
    dummy  = forms.CharField(max_length=100)


def create_qr2019(request):
    # process form data if POST request
    if request.method == 'POST':
        # create form instance
        form = QR2019Form(request.POST)
        # TODO: validate address with LOB API HERE
        # confirm form values are valid
        if form.is_valid():
            # print("form.cleaned_data['architect']: ", form.cleaned_data['architect'])
            print('form.cleaned_data: ', form.cleaned_data),
            QR2019.objects.create(
                dummy = form.cleaned_data['lobbyist_name'],
            )
            # messages.info(request, "New Project Created")
            return redirect('/lobqr19/')

    else:
        form = QR2019Form()
    
    context = {
        'form': form,
    }
    return render(request, 'pages/lobqr19-create.html', context)
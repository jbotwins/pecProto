from django.shortcuts import render, redirect
from django import forms

# Create your views here.
from .models import LobReg2019


class LobReg2019Form(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=250)
    phone = forms.CharField(max_length=100)
    address = forms.CharField(max_length=250)


def create_lobreg2019(request):
    # process form data if POST request
    if request.method == 'POST':
        # create form instance
        form = LobReg2019Form(request.POST)
        # TODO: validate address with LOB API HERE
        # confirm form values are valid
        if form.is_valid():
            # print("form.cleaned_data['architect']: ", form.cleaned_data['architect'])
            print('form.cleaned_data: ', form.cleaned_data),
            LobReg2019.objects.create(
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                email = form.cleaned_data['email'],
                phone = form.cleaned_data['phone'],
                address = form.cleaned_data['address'],
            )
            # messages.info(request, "New Project Created")
            return redirect('/lobreg19/')

    else:
        form = LobReg2019Form()
    
    context = {
        'form': form,
    }
    return render(request, 'pages/lobreg19-create.html', context)
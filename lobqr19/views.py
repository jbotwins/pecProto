from django.shortcuts import render, redirect
from django import forms

# Create your views here.
from .models import QR2019

# class Lobqr19DetailView():
#forms as classes

class QR2019Form(forms.Form):
#   changed from 'architect' to 'assign_an_architect'
#   assign_an_architect = forms.ModelChoiceField(queryset=Architect.objects.all())
    
#   changed from 'client' to 'assign_a_client'
#   assign_a_client = forms.ModelChoiceField(queryset=Client.objects.all())

#     changed from 'name_proj' to 'project_name'
    lobbyist_name  = forms.CharField(max_length=100)
#     changed from 'address' to 'project_address'
    # project_address  = forms.CharField(max_length=100)

    # start_date  = forms.DateField(widget=forms.SelectDateWidget)
    # end_date  = forms.DateField(widget=forms.SelectDateWidget)


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
                lobbyist_name = form.cleaned_data['lobbyist_name'],
            )
            # messages.info(request, "New Project Created")
            return redirect('/lobqr19/')

    else:
        form = QR2019Form()
    
    context = {
        'form': form,
    }
    return render(request, 'pages/lobqr19-create.html', context)
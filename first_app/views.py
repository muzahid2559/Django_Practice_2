from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician, Album
from first_app import forms

# Create your views here.

def index(request):
    # SELECT * FROM Musician ORDER BY first_name
    musician_list = Musician.objects.order_by('first_name')
    diction = {'text_1':'This is a list of Musician', 'musician': musician_list}
    return render(request,'first-app/index.html',context=diction)


def form(request):
    new_form = forms.user_form()
    diction = {'Djano_form':new_form, 'heading_for_Djano':'This form is created using django library'}

    if request.method == 'POST':
        new_form = forms.user_form(request.POST)

        if new_form.is_valid():
            user_name = new_form.cleaned_data['user_name']
            user_dob = new_form.cleaned_data['user_dob']
            user_email = new_form.cleaned_data['user_email']


            diction.update({'user_name':user_name})
            diction.update({'user_dob':user_dob})
            diction.update({'user_email':user_email})
            diction.update({'form_submited' : 'Yes'})

    return render(request,'first-app/form.html',context=diction)

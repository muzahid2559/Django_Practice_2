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
    return render(request,'first-app/form.html',context=diction)

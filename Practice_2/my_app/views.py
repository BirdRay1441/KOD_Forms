from django.shortcuts import render
from . import forms

def index(request):
    return render(request, 'my_app/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Дело сделано!")
            print("Name: " + form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("Text: " + form.cleaned_data['text'])

    context = {'form': form}
    return render(request, 'my_app/form_page.html', context=context)

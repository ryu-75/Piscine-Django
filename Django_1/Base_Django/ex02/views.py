import logging
from django.conf import settings 
from django.shortcuts import render, redirect
from . import forms


logger = logging.getLogger('django')
def get_form(request):
    context = {}
    context['form'] = forms.Formular
    if request.method == "POST":
        # create a form instance and populate it with data form the request:
        form = forms.Formular(request.POST)
        # check whether it's valid:
        if form.is_valid():
            logger.info(f"Firstname: {form.cleaned_data['firstname']}")
            logger.info(f"Lastname: {form.cleaned_data['lastname']}")
            logger.info(f"Age: {form.cleaned_data['age']}")
            logger.info(f"Email: {form.cleaned_data['email']}")
            # process the data in form.cleaned_data as required
            # ... redirect to a new URL:
        return redirect('/ex02')
    # Displaying the log file history"
    try:
        with open(settings.HISTORY_LOG_FILE, 'r') as f:
            historys = [line for line in f.readlines()]
    except:
        historys = []
    
    return render(request, "ex02/form.html", {'form': forms.Formular(), 'historys': historys})
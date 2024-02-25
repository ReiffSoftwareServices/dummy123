# import re
# from django.http import HttpResponse
from django.shortcuts import render
from django.utils.timezone import datetime

from django.shortcuts import redirect
from hello.forms import LogMessageForm, LogMessageForm2, AnmeldungForm
from hello.models import LogMessage

from django.views.generic import ListView

def runOldVersion(request):
    # return render(request, "hello/index.html")
    formAnmeldung = AnmeldungForm(request.POST or None)
    if request.method == "POST":
        if formAnmeldung.is_valid():
            results = AnmeldungForm(request.POST)
            results.save()
            return redirect("mvp")
    else:
        return render(request, "hello/index.html", {"formAnmeldung": formAnmeldung})
        
class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")


def hello_there(request, name):
    print(request.build_absolute_uri())
    return render(
        request,
        'hello/hello_there.html',
        {
            'name' : name, 
            'date': datetime.now()
        }
    )
    
# Add this code elsewhere in the file:
def log_message(request):
    form = LogMessageForm(request.POST or None)
    form2 = LogMessageForm2(request.POST or None)

    if request.method == "POST":
        submitted_form_name = request.POST.get('submit_button')
        if submitted_form_name == 'submit_form1':
            if form.is_valid():
                message = form.save(commit=False)
                message.log_date = datetime.now()
                message.source = "A"
                message.save()
                return redirect("home")
        elif submitted_form_name == 'submit_form2':
            if form2.is_valid():
                message = form2.save(commit=False)
                message.log_date = datetime.now()
                message.source = "B"
                message.save()
                return redirect("home")
    else:
        return render(request, "hello/log_message.html", {"form": form, "form2": form2})
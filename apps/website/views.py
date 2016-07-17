from django.shortcuts import render_to_response
from django.template.context import RequestContext
# Create your views here.

def home(request):
    context = RequestContext(request,{'user':request.user})
    return render_to_response("home.html",context_instance=context)

def about(request):
    return render_to_response("about.html", {})

def contact(request):
    return render_to_response("contact.html", {})

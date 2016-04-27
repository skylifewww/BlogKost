from django.contrib import auth
from django.shortcuts import render_to_response
from article.views import return_path_f


# Create your views here.
def slider(request):

    return_path_f(request)

    return render_to_response("slider.html", {'username': auth.get_user(request).username})


def tutorials(request):

    return_path_f(request)

    return render_to_response("tutorials.html", {'username': auth.get_user(request).username})


def contact(request):

    return_path_f(request)

    return render_to_response("contact.html", {'username': auth.get_user(request).username})


def portfolio(request):

    return_path_f(request)

    return render_to_response("portfolio.html", {'username': auth.get_user(request).username})

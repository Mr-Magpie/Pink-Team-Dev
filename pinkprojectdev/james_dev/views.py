from django.shortcuts import render

from .aggregator_test import aggregate

# Create your views here.


def james_dev(request):
    title = "Home Page"
    user = request.user
    l = []
    for i in aggregate():
        l.append(i.to_string())

    print(l)

    context = {
        "template_title": title,
        "user": user,
        "article_list": l,
    }

    return render(request, "temp/jamesdev.html", context)


def james_dev2(request):
    title = "Test Page 1"
    user = request.user


    context = {
        "template_title" : title,
        "user" :user,
    }

    return render(request, "jamesdev2.html", context)


def james_dev3(request):
    title = "Test Page 2"
    user = request.user


    context = {
        "template_title" : title,
        "user" :user,
    }

    return render(request, "jamesdev3.html", context)
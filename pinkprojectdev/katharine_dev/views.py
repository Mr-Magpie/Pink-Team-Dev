from django.shortcuts import render

# Create your views here.


def katharine_dev(request):

    title = "Home Page"
    user = request.user

    context = {
        "template_title" : title,
        "user" :user,
    }


    return render(request, "katharinedev.html", context)





def katharine_dev2(request):
    title = "Test Page 1"
    user = request.user


    context = {
        "template_title" : title,
        "user" :user,
    }

    return render(request, "katharinedev2.html", context)


def katharine_dev3(request):
    title = "Test Page 2"
    user = request.user


    context = {
        "template_title" : title,
        "user" :user,
    }

    return render(request, "katharinedev3.html", context)
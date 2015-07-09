from django.shortcuts import render

# Create your views here.


def kang_dev(request):

    title = "Home Page"
    user = request.user

    context = {
        "template_title" : title,
        "user" :user,
    }


    return render(request, "kangdev.html", context)





def kang_dev2(request):
    title = "Test Page 1"
    user = request.user


    context = {
        "template_title" : title,
        "user" :user,
    }

    return render(request, "kangdev2.html", context)


def kang_dev3(request):
    title = "Test Page 2"
    user = request.user


    context = {
        "template_title" : title,
        "user" :user,
    }

    return render(request, "kangdev3.html", context)
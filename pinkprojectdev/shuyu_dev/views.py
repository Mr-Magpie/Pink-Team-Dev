from django.shortcuts import render

# Create your views here.


def shuyu_dev(request):

    title = "Home Page"
    user = request.user

    context = {
        "template_title" : title,
        "user" :user,
    }


    return render(request, "shuyudev.html", context)





def shuyu_dev2(request):
    title = "Test Page 1"
    user = request.user


    context = {
        "template_title" : title,
        "user" :user,
    }

    return render(request, "shuyudev2.html", context)


def shuyu_dev3(request):
    title = "Test Page 2"
    user = request.user


    context = {
        "template_title" : title,
        "user" :user,
    }

    return render(request, "shuyudev3.html", context)
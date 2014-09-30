import datetime

from django.http import HttpResponse
# Create your views here.


def index(request):
    request.session.set_test_cookie()
    return HttpResponse("Hello, world. You are at the user_tracking index.")


def detail(request, user_id):
    return HttpResponse("You're looking at user: %s" % user_id)


def name(request, user_id):
    return HttpResponse("You're viewing the name of user: %s" % user_id)


def time(request, user_id):
    return HttpResponse("You're viewing the access time of user: %s" % user_id)


def root(request):

    return HttpResponse("End of page, need to display date, time, URL user has been forwarded to")


def redirect(request):

    return HttpResponse("Great!")






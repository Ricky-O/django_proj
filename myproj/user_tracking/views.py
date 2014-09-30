import datetime
from models import User, Access

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
    #could make this output much better and more appealing
    for obj in User.objects.all():
        return HttpResponse("Last visited: %s" % User.print_all(User.objects.all()))


def redirect(request):
    user1 = User.objects.get(pk=1)
    u = User.print_all(user1)
    #could make this output much better and more appealing
    return HttpResponse("Last visited: %s" % u)






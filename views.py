from django.http import Http404
from vl.models import Lecture
from lectures.vl.views import urlrw as vl_urlrw


def urlrw(request, txt, template_name=None):
    if Lecture.objects.filter(slug__istartswith=txt[0:50]).exists():
        lec = Lecture.objects.filter(slug__istartswith=txt[0:50])[0]
        return vl_urlrw(request, lec.slug, template_name)

    raise Http404
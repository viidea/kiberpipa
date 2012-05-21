from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.views.decorators.cache import cache_control

from django.http import HttpResponse

import Image

from vl.models import Lecture
from lectures.vl.views import urlrw as vl_urlrw


def urlrw(request, txt, template_name=None):
    text = txt[0:50].replace('.', '')
    if Lecture.objects.filter(slug__istartswith=text).exists():
        lec = Lecture.objects.filter(slug__istartswith=text)[0]
        return vl_urlrw(request, lec.slug, template_name)

    raise Http404


IMAGE_I_SIZE = 500, 500
@cache_control(must_revalidate=False, max_age=86400)
def image_i(request, slug, part_id=None):
    text = slug[0:50].replace('.', '')
    if Lecture.objects.filter(slug__istartswith=text).count():
        lec = Lecture.objects.filter(slug__istartswith=text).order_by('id')[0]
    else:
        raise Http404


    if lec.get_screenshot_att():
        image = Image.open(lec.get_screenshot_att().render.mnt)
        image.thumbnail(IMAGE_I_SIZE,Image.ANTIALIAS)

        response = HttpResponse(mimetype="image/jpeg")
        image.save(response, "JPEG")
        return response
    else: 
        raise Http404


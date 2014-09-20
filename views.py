from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.views.decorators.cache import cache_control

from django.http import HttpResponse

from PIL import Image

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
    try:
        lec = Lecture.objects.filter(slug__istartswith=text).order_by('id')[0]
    except IndexError:
        raise Http404

    screenshot = lec.get_screenshot()
    if screenshot:
        image = Image.open(screenshot.render.mnt)
        image.thumbnail(IMAGE_I_SIZE,Image.ANTIALIAS)

        response = HttpResponse(mimetype="image/jpeg")
        image.save(response, "JPEG")
        return response
    else: 
        raise Http404


from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'(?i)^media/(?P<txt>[^/]+)/(play.html|'')$','lectures._custom.kiberpipa.views.urlrw'), 
	(r'(?i)^media/(?P<slug>[^/]+)/image-i.jpg$','lectures._custom.kiberpipa.views.image_i'),
	(r'(?i)^media/(?P<slug>[^/]+)/image-s.jpg$','lectures._custom.kiberpipa.views.image_i'),
)
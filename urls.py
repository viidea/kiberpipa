from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'(?i)^media/(?P<txt>[^/]+)/(play.html|'')$','lectures._custom.kiberpipa.views.urlrw'), 
)
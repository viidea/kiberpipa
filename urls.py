from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^(izven|pot|su)/(?P<txt>[^/]+)/(play.html|'')$','vl.views.urlrw'), 
)
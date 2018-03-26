from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib import admin

import backbone

admin.autodiscover()
backbone.autodiscover()

from backbone.tests.views import homepage

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^backbone/', backbone.site.urls),
    url(r'^$', homepage, name='tests-homepage'),
]

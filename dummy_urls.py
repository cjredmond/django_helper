from django.conf.urls import url
from django.contrib import admin
from dummy_views import FirstView, SecondView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', FirstView.as_view(), name='first_view'),
    url(r'^resume/$', SecondView.as_view(), name='second_view')
]

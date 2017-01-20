
from django.conf.urls import url
from django.contrib import admin
from test_app.views import PostDetailView, PostListView, PostCreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^post/(?P<pk>\d+)$', PostDetailView.as_view(), name="post_detail_view"),
	url(r'^post/new/$', PostCreateView.as_view(), name="post_create_view"),
	url(r'^posts/$', PostListView.as_view(), name="post_list_view")
]

from django.conf.urls import url
from django.contrib import admin
# from test_app.views import PostDetailView, PostListView, PostCreateView, PostUpdateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

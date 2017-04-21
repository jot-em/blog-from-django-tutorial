from django.conf.urls import url
from . import views
from django.contrib.auth.views import login
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^about/$', views.about, name='about'),
    # url(r'^login/$', views.login, name='login'),
    url(r'^login/$', login, kwargs={'template_name': 'blog/login.html'}, name='login'),
    url(r'^post/category/$', views.category, name='category'),
    url(r'^accounts/profile/$', RedirectView.as_view(url='/panel/nowy_post')),
    url(r'^panel/$', views.panel, name='panel'),
   
    # po zalogowaniu
    url(r'^panel/nowy_post$', views.post_new, name='post_new'),

]

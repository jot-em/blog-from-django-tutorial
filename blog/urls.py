from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^about/$', views.about, name='about'),
    url(r'^login/$', login, kwargs={'template_name': 'blog/login.html'}, name='login'),
    url(r'^logout/$', logout,{'next_page': '/about'}, name='logout_user'),
    url(r'^category/(?P<ctg>[a-z]+)/$', views.category, name='category'),
    url(r'^accounts/profile/$', RedirectView.as_view(url='/panel/nowy_post')),
    url(r'^panel/$', views.panel, name='panel'),
    url(r'^register[/]?$', views.register, name='register'),
    url(r'^register/success/$', views.register_success, name='register_success'),

    # po zalogowaniu
    url(r'^panel/nowy_post$', views.post_new, name='post_new'),

]

from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /manager/
    url(r'^$',views.index,name="index"),
    url(r'add/(?P<module_name>.*)/(?P<parent_id>[0-9]+)/(?P<desc>.*)/$', views.add_module, name='add_module'),
    url(r'tree/',views.show_module_tree,name='show_module_tree'),
    url(r'login/',views.login,name='login')
]
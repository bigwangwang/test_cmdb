from django.conf.urls import url
from host import views


urlpatterns = [
    url(r'list.html', views.list),
    url(r'add.html', views.add),
    url(r'edit/(\d+)', views.edit),
    url(r'del', views.delete),
]

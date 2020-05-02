from django.urls import path, re_path
from . import views

urlpatterns = [
	re_path('^$', views.IndexView.as_view(), name='index'),
	re_path('^registration/$', views.UserFormView.as_view(), name='registration'),
	re_path('^add/$', views.CreateAlbum.as_view(), name='album-add'),
	re_path('^(?P<pk>[0-9]+)/$', views.UpdateAlbum.as_view(), name='album-update'),
	re_path('^(?P<pk>[0-9]+)/Delete/$', views.DeleteAlbum.as_view(), name='album-delete'),
	#re_path('^first/$', views.first, name="first"),
]
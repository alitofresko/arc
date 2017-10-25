from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /member_list
    url(r'^member_list/$', views.member_list, name='member_list'),
    url(r'^members/$', views.MemberListView.as_view(), name='members'),
    url(r'^member/(?P<pk>\d+)$', views.MemberDetailView.as_view(), name='member-detail'),

]

from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path(r'', views.SchoolListView.as_view(), name='list'),
    path(r'(?P<pk>\d+)/', views.SchoolDetailView.as_view(), name='detail'),
    path(r'create/', views.SchoolCreateView.as_view(),name='create'),
    path(r'update/(?P<pk>\d+)', views.SchoolUpdateView.as_view(),name='update'),
    path(r'delete/(?P<pk>\d+)', views.SchoolDeleteView.as_view(),name='delete')
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirHome),
    path('shows/new', views.showForm),
    path('shows/create', views.addShow),
    path('shows/<int:this_show>', views.grabShow),
    path('shows', views.allShows),
    path('shows/<int:show_id>/edit', views.editShow),
    path('shows/<int:show_id>/update', views.updateShow),
    path('shows/<int:show_id>/destroy', views.destroyShow)
]
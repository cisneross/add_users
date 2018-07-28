from django.urls import path
#DO this!!!!! up above
from . import views

urlpatterns = [
    path('users',views.table),
    path('users/new',views.add),
    path('process',views.process),
    path('<int:id>/destroy',views.destroy),
    path('users/<int:id>/edit', views.edit),
    path('users/update',views.process_edit),
    path('users/<int:id>',views.show),
]
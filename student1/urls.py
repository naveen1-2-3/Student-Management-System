from . import views
from django.urls import path

app_name = 'student1'
urlpatterns = [
    path("create/",views.create_view,name="create"),
    path("",views.show_view,name="show"),
    path("update/<int:pk>/",views.update_view,name="update"),
    path("delete/<int:pk>/",views.delete_view,name="delete"),
]

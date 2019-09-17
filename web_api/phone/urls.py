from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("list", views.get_phone_list, name="list"),
    path("phones/<int:p_id>", views.get_phone_by_id, name="detail")
]

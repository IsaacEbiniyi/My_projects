from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("mental", views.ment, name="mental"),
    path("home", views.index, name="home"),
    path("news", views.news, name="news"),
    path("health", views.healthy_foods, name="health"),
    path("stuff", views.stuffs, name="stuff"),
    path("spinach", views.features_of_spinach, name="spinach"),
    path("garlic", views.features_of_garlic, name="garlic"),
    path("lemons", views.features_of_lemon, name="lemons"),
    path("beetroot", views.features_of_beetroots, name="beetroot"),
    path("chocolate", views.features_chocolates, name="chocolate"),
    path("lentils", views.features_lentils, name="lentils"),
    path("raspberry", views.features_raspberry, name="raspberry"),
    path("walnut", views.features_walnut, name="walnut"),
    path("salmon", views.features_salmon, name="salmon"),
    path("avocado", views.features_avocado, name="avocado"),
    path("home_page", views.main, name="home_page"),
    path("zip_code", views.zip_code, name="zip_code")

]
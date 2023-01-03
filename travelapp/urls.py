from django.urls import path
from .import views

urlpatterns = [
    path('',views.Home.as_view(),name="home_page"),
    path('index',views.Index.as_view(),name="index_page"),
    path('about',views.About.as_view(),name="about_page"),
    path('contact',views.Contact.as_view(),name="contact_page"),
    path('details',views.Details.as_view(),name="details_page"),
    path('login',views.Login.as_view(),name="login_page"),
    path('logout',views.logout,name="logout_page"),
]
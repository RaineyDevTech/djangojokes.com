from django.urls import path

from .views import AboutUsView, HomePageView

app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('about_us/', AboutUsView.as_view(), name='about-us'),
]
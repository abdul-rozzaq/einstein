



from django.urls import path

from project.views import home_page, videos_page, player_page


urlpatterns = [
    path('', home_page, name='home'),
    path('videos/<int:pk>/', videos_page, name='videos'),
    path('player/<int:pk>/', player_page, name='player'),
]
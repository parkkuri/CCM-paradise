from django.urls import path, re_path
from .views import accompantiment_list, accompantiment_detail, SearchView

urlpatterns = [
    # http://127.0.0.1:8000/musics/?page=2
    path('', accompantiment_list.as_view(), name='list' ),
    # http://127.0.0.1:8888/musics/1/?pitch_id=1
    path('musics/<int:pk>/', accompantiment_detail.as_view(), name='detail'),
    path('musics/search', SearchView.as_view(), name='search'),



]

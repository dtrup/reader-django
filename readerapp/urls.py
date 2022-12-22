from django.urls import path
from . import views

app_name = 'reader'

urlpatterns = [
    path('texts/', views.TextListView.as_view(), name='text_list'),
    path('texts/<slug:text_id>/', views.TextDetailView.as_view(), name='text_detail'),
    path('texts/<slug:text_id>/<int:chapter_number>', views.ChapterListView.as_view(), name='sentence_list')
]
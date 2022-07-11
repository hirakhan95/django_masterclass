from django.urls import path
from . import views

urlpatterns = [
    path('<int:pg_num>', views.page_num_view),
    path('<str:topic>/', views.news_view),
    path('<int:num1>/<int:num2>/', views.add_func),
]

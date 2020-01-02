from django.urls import path
from . import views

app_name = 'polls'

#polls/ 이후 url 모두 처리

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:question_id>/', views.detail, name='detail'), #views의 detail 함수
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

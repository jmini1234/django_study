from django.urls import path
from . import views #어떤 view를 제공할 것인지

app_name = 'blog'

urlpatterns = [

    path('index/',views.index,name='index'), #마지막에 / 안쓰면 안됨 
    path('create/',views.create,name='create'), #create는 parameter 넘겨주지 않아도 된다.
    path('<int:pk>/update/',views.update,name='update'),
    path('<int:pk>/delete/',views.delete,name='delete'),
    path('<int:pk>/',views.detail,name='detail'), #detail은 따로 url 없이

]

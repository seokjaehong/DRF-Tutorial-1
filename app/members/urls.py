from django.urls import path, include

from members import views
from .apis import UserList, UserDetail

app_name = 'members'
urlpatterns = [
    path('', UserList.as_view()),
    path('<int:pk>/', UserDetail.as_view()),
]

from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('api/guides', views.GuideList.as_view(), name='guide_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/guides/<int:pk>', views.GuideDetail.as_view(), name='guide_detail'), # api/contacts will be routed to the ContactDetail view for handling
    path('api/guides/upload', views.upload, name ='upload'),
    path('api/user', views.UserList.as_view(), name='user_list'),
    path('api/user/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('api/user/login', csrf_exempt(views.check_login), name="check_login") # will be routed to the check_login function for auth
]

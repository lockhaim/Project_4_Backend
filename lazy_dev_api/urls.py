from django.urls import path
from . import views

urlpatterns = [
    path('api/guides', views.GuideList.as_view(), name='guide_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/guides/<int:pk>', views.GuideDetail.as_view(), name='guide_detail'), # api/contacts will be routed to the ContactDetail view for handling
]

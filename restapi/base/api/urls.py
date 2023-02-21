from django.urls import path
from . import views

urlpatterns = [
    path('initiate-call/',views.initiateCall),
    path('call-report',views.getData_with_number),
    path('update-call-log/<str:pk>/',views.update_callLog),
    path('delete-call-log/<str:pk>/',views.delete_callLog)
]
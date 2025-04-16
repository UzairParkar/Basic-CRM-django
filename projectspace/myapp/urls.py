
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('',views.home,name='home'),
    # path('login/',views.login_user,name='login'), <- integrated into the hoem route
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),

    path('record/<int:pk>',views.detail_record,name='detail'),
    path('delete/<int:pk>',views.delete_record,name='delete'),
    path('add_record/',views.add_record,name='add'),
    path('update_record/<int:pk>',views.update_record,name='update')
]


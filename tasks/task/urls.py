from django.urls import path
from . import views


urlpatterns=[ # function based urls
    #path('',home,name='homepage'),
    #path('add/',add_task,name='add_task'),
    #path('task/<int:task_pk>',view_task,name='view_task'),
    #path('task/<int:task_pk>/update/',update_task,name='update_task'),
    #path('task/<int:task_pk>/delete/',delete_task,name='delete_task'),"""
    #class based urls
    path('',views.HomePageView.as_view(),name='homepage'),
    path('add/',views.TaskCreateView.as_view(),name='add_task'),
    path('task/<int:pk>/',views.TaskDetailView.as_view(),name='view_task'),
    path('task/<int:pk>/update/',views.TaskUpdateView.as_view(),name='update_task'),
    path('task/<int:pk>/delete/',views.TaskDeleteView.as_view(),name='delete_task'),
    path('settings/',views.SettingsView.as_view(),name='settings'),
]
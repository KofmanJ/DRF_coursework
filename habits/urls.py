from django.urls import path

from habits.apps import HabitsConfig
from habits.views.habits import HabitListAPIView, HabitDetailAPIView, HabitCreateAPIView, HabitUpdateAPIView, \
    HabitDeleteAPIView
from habits.views.nice_habit import NiceHabitListAPIView, NiceHabitDetailAPIView, NiceHabitCreateAPIView, \
    NiceHabitUpdateAPIView, NiceHabitDeleteAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('habit/', HabitListAPIView.as_view(), name='habit_list'),
    path('habit/<int:pk>/', HabitDetailAPIView.as_view(), name='habit_detail'),
    path('habit/create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habit/delete/<int:pk>/', HabitDeleteAPIView.as_view(), name='habit_delete'),

    path('nice_habit/', NiceHabitListAPIView.as_view(), name='habit_list'),
    path('nice_habit/<int:pk>/', NiceHabitDetailAPIView.as_view(), name='habit_detail'),
    path('nice_habit/create/', NiceHabitCreateAPIView.as_view(), name='habit_create'),
    path('nice_habit/update/<int:pk>/', NiceHabitUpdateAPIView.as_view(), name='habit_update'),
    path('nice_habit/delete/<int:pk>/', NiceHabitDeleteAPIView.as_view(), name='habit_delete'),
]

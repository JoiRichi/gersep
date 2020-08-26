from django.urls import path
from . import views

urlpatterns = [
    path('exam', views.assignment_page, name='index_page'),
    path('success', views.success_page, name='success_page'),
    path('submitted', views.get_list_of_submission, name='submitted_page'),
    path('scores', views.get_scores, name='scores_page'),
]
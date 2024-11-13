from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Ruta para el panel de inicio


    path('create/', views.create_survey_view, name='create_survey'),
    path('manage_questions/', views.question_management_view, name='manage_questions'),  # URL para gestionar preguntas





    #antiguo
    path('activate/', views.activate_survey_view, name='activate_survey'),
    path('results/', views.view_results, name='view_results'),
    
]

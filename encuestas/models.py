# models.py
from django.db import models

class Survey(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nombre de la Encuesta")
    description = models.TextField(blank=True, verbose_name="Descripción de la Encuesta")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    def __str__(self):
        return self.name

class Question(models.Model):
    QUESTION_TYPES = [
        ('text', 'Respuesta Única'),
        ('multiple_choice', 'Selección Múltiple')
    ]

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="questions", verbose_name="Encuesta")
    text = models.CharField(max_length=255, verbose_name="Texto de la Pregunta")
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES, verbose_name="Tipo de Pregunta")
    choices = models.JSONField(null=True, blank=True, verbose_name="Opciones de Selección Múltiple")

    def __str__(self):
        return f"{self.text} ({self.question_type})"

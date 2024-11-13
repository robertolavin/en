# forms.py
from django import forms
from .models import Survey, Question

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['name', 'description']

class QuestionForm(forms.ModelForm):
    choices = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Opciones separadas por comas (solo para selección múltiple)'}),
        label="Opciones"
    )

    class Meta:
        model = Question
        fields = ['text', 'question_type', 'choices']  # Excluir 'survey' del formulario

    def clean_choices(self):
        choices = self.cleaned_data.get('choices')
        if self.cleaned_data.get('question_type') == 'multiple_choice':
            if choices:
                return [choice.strip() for choice in choices.split(',') if choice.strip()]
            else:
                raise forms.ValidationError("Debe proporcionar al menos una opción para selección múltiple.")
        return None


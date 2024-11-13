# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Survey, Question
from .forms import SurveyForm, QuestionForm
from django.urls import reverse

def create_survey_view(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_survey')  # Redirige de nuevo al formulario de creación
    else:
        form = SurveyForm()
    return render(request, 'encuestas/create_survey.html', {'form': form})

# Vista para gestionar preguntas de una encuesta específica
def question_management_view(request):
    surveys = Survey.objects.all()
    selected_survey_id = request.GET.get('survey_id')
    selected_survey = None
    questions = None

    # Si hay una encuesta seleccionada, obtén las preguntas
    if selected_survey_id:
        selected_survey = get_object_or_404(Survey, id=selected_survey_id)
        questions = Question.objects.filter(survey=selected_survey)

    # Manejo del formulario para agregar o editar preguntas
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.survey = selected_survey  # Asigna la encuesta seleccionada directamente aquí
            question.save()
            # Usar `reverse` para construir la URL con el nombre y pasar el parámetro `survey_id`
            return redirect(f"{reverse('manage_questions')}?survey_id={selected_survey_id}")
    else:
        form = QuestionForm()

    return render(request, 'encuestas/manage_questions.html', {
        'surveys': surveys,
        'selected_survey': selected_survey,
        'questions': questions,
        'form': form
    })

















### REVISAR/ELIMINAR
# Vista para activar una encuesta
def activate_survey_view(request):
    # Esta vista mostrará una lista de encuestas con un botón de activación
    return render(request, 'encuestas/activate_survey.html')

# Vista para ver los resultados de las encuestas
def view_results(request):
    # Esta vista mostrará los resultados de las encuestas
    return render(request, 'encuestas/view_results.html')

# Vista para el panel de inicio
def dashboard(request):
    # Vista de inicio o panel principal
    return render(request, 'encuestas/dashboard.html')


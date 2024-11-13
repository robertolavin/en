# Generated by Django 3.2.20 on 2024-11-13 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0003_auto_20241112_2344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveydetail',
            name='survey',
        ),
        migrations.AddField(
            model_name='survey',
            name='description',
            field=models.TextField(blank=True, verbose_name='Descripción de la Encuesta'),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='SurveyDetail',
        ),
    ]
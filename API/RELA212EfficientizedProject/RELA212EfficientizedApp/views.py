from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import *
from .models import *

class ExamsViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializerClass = ExamSerializer

class StudyGuidesViewSet(viewsets.ModelViewSet):
    queryset = StudyGuide.objects.all()
    serializerClass = StudyGuideSerializer

class QuestionGroupsViewSet(viewsets.ModelViewSet):
    queryset = QuestionGroup.objects.all()
    serializerClass = QuestionGroupSerializer

class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializerClass = QuestionSerializer

class AnswerHintsViewSet(viewsets.ModelViewSet):
    queryset = AnswerHint.objects.all()
    serializerClass = AnswerHintSerializer

class AnswersViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializerClass = AnswerSerializer

class AnswerLocationsViewSet(viewsets.ModelViewSet):
    queryset = AnswerLocation.objects.all()
    serializerClass = AnswerLocationSerializer

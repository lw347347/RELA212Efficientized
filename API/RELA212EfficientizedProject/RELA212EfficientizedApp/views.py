from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import *
from .models import *

class ExamsViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class StudyGuidesViewSet(viewsets.ModelViewSet):
    queryset = StudyGuide.objects.all()
    serializer_class = StudyGuideSerializer

class QuestionGroupsViewSet(viewsets.ModelViewSet):
    queryset = QuestionGroup.objects.all()
    serializer_class = QuestionGroupSerializer

class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializerClass = QuestionSerializer

class AnswerHintsViewSet(viewsets.ModelViewSet):
    queryset = AnswerHint.objects.all()
    serializer_class = AnswerHintSerializer

class AnswersViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class AnswerLocationsViewSet(viewsets.ModelViewSet):
    queryset = AnswerLocation.objects.all()
    serializer_class = AnswerLocationSerializer

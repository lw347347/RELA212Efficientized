from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['studyGuideId']

class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['questionGroupId']

class AnswerHintsViewSet(viewsets.ModelViewSet):
    queryset = AnswerHint.objects.all()
    serializer_class = AnswerHintSerializer

class AnswersViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['questionId']

class AnswerLocationsViewSet(viewsets.ModelViewSet):
    queryset = AnswerLocation.objects.all()
    serializer_class = AnswerLocationSerializer

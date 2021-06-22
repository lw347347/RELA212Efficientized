from rest_framework import serializers
from .models import *

class ExamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exam
        fields = (
            'examId',
            'examNumber',
            'examStartDate',
            'examEndDate',
        )

class StudyGuideSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudyGuide
        fields = (
            'studyGuideId',
            'examId',
            'name',
            'typeOfStudyGuide',
            'file',
            'dateOfAssignment',
            'studyGuideNumber',
        )

class QuestionGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestionGroup
        fields = (
            'questionGroupId',
            'studyGuideId',
            'scriptureBookName',
            'scriptureChapterNumber',
            'countOfQuestions',
            'questionGroupNumber',
        )

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = (
            'questionId',
            'questionGroupId',
            'questionText',
            'questionNumber',
        )

class AnswerHintSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnswerHint
        fields = (
            'answerHintId',
            'questionId',
            'answerHintType',
            'scriptureBookName',
            'scriptureChapterNumber',
            'scriptureVerseNumber',
            'handoutCharacterStart',
            'handoutCharacterEnd',
        )
class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = (
            'answerId',
            'questionId',
            'answerText',
        )
class AnswerLocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnswerLocation
        fields = (
            'answerLocationId',
            'answerId',
            'answerLocationType',
            'scriptureBookName',
            'scriptureChapterNumber',
            'scriptureVerseNumber',
            'handoutCharacterStart',
            'handoutCharacterEnd',
        )
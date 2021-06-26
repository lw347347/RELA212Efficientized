from rest_framework import serializers
from rest_framework.fields import FileField
from .models import *
from .parsePDF import parsePDF

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
    exam = ExamSerializer(
        many=False,
        read_only=True
    )
    examId = serializers.IntegerField(
        write_only=True
    )
    file = FileField()

    class Meta:
        model = StudyGuide
        fields = (
            'studyGuideId',
            'exam',
            'examId',
            'name',
            'typeOfStudyGuide',
            'file',
            'dateOfAssignment',
            'studyGuideNumber',
        )

    def create(self, formData):
        print(formData)
        examId = Exam.objects.filter(pk=formData['examId']).first()
        studyGuide = StudyGuide.objects.create(
            examId = examId,
            name = formData["name"],
            typeOfStudyGuide = formData["typeOfStudyGuide"],
            dateOfAssignment = formData["dateOfAssignment"],
            file = formData["file"]
        )
        studyGuide.save()

        # Parse the PDFs
        parsePDF(studyGuide)

        return studyGuide

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
from rest_framework import serializers
from rest_framework.fields import FileField
from rest_framework.relations import PrimaryKeyRelatedField
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

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = (
            'answerId',
            'questionId',
            'answerText',
        )
    def update(self, instance, validated_data):
        instance.answerText = validated_data.get('answerText', instance.answerText)
        instance.save()
        return instance

class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=False)
    class Meta:
        model = Question
        fields = (
            'questionId',
            'questionGroupId',
            'questionText',
            'questionNumber',
            'answer',
        )

class QuestionGroupSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = QuestionGroup
        fields = [
            'questionGroupId',
            'studyGuideId',
            'scriptureBookName',
            'scriptureChapterNumber',
            'countOfQuestions',
            'questionGroupNumber',
            'questions'
        ]

class StudyGuideSerializer(serializers.HyperlinkedModelSerializer):
    exam = ExamSerializer(
        many=False,
        read_only=True
    )
    examId = serializers.IntegerField(
        write_only=True
    )
    file = FileField()
    questionGroups = QuestionGroupSerializer(
        many=True
    )

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
            'questionGroupSplitter',
            'questionGroupBeginning',
            'questionGroups',
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
        parsePDF(studyGuide, formData["file"], questionGroupSplitter=formData["questionGroupSplitter"])

        return studyGuide

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
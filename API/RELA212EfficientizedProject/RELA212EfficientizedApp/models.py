from django.db import models

# Create your models here.
class Exam(models.Model):
    examId = models.AutoField(primary_key=True)
    examNumber = models.IntegerField(default=None, blank=True, null=True)
    examStartDate = models.DateField(default=None, blank=True, null=True)
    examEndDate = models.DateField(default=None, blank=True, null=True)

class StudyGuide(models.Model):
    studyGuideId = models.AutoField(primary_key=True)
    examId = models.ForeignKey(Exam, on_delete=models.CASCADE, default=None, blank=True, null=True)
    name = models.TextField(default=None, blank=True, null=True)
    typeOfStudyGuide = models.TextField(default=None, blank=True, null=True)
    file = models.FileField(default=None, blank=True, null=True)
    dateOfAssignment = models.DateField(default=None, blank=True, null=True)
    studyGuideNumber = models.IntegerField(default=None, blank=True, null=True)

class QuestionGroup(models.Model):
    questionGroupId = models.AutoField(primary_key=True)
    studyGuideId = models.ForeignKey(StudyGuide, on_delete=models.CASCADE, default=None, blank=True, null=True)
    scriptureBookName = models.TextField(default=None, blank=True, null=True)
    scriptureChapterNumber = models.IntegerField(default=None, blank=True, null=True)
    countOfQuestions = models.IntegerField(default=None, blank=True, null=True)
    questionGroupNumber = models.IntegerField(default=None, blank=True, null=True)

class Question(models.Model):
    questionId = models.AutoField(primary_key=True)
    questionGroupId = models.ForeignKey(QuestionGroup, on_delete=models.CASCADE, default=None, blank=True, null=True)
    questionText = models.TextField(default=None, blank=True, null=True)
    questionNumber = models.IntegerField(default=None, blank=True, null=True)

class AnswerHint(models.Model):
    answerHintId = models.AutoField(primary_key=True)
    questionId = models.ForeignKey(Question, on_delete=models.CASCADE, default=None, blank=True, null=True)
    answerHintType = models.TextField(default=None, blank=True, null=True)
    scriptureBookName = models.TextField(default=None, blank=True, null=True)
    scriptureChapterNumber = models.IntegerField(default=None, blank=True, null=True)
    scriptureVerseNumber = models.IntegerField(default=None, blank=True, null=True)
    handoutCharacterStart = models.IntegerField(default=None, blank=True, null=True)
    handoutCharacterEnd = models.IntegerField(default=None, blank=True, null=True)

class Answer(models.Model):
    answerId = models.AutoField(primary_key=True)
    questionId = models.OneToOneField(Question, on_delete=models.CASCADE, default=None, blank=True, null=True)
    answerText = models.TextField(default=None, blank=True, null=True)

class AnswerLocation(models.Model):
    answerLocationId = models.AutoField(primary_key=True)
    answerId = models.OneToOneField(Answer, on_delete=models.CASCADE, default=None, blank=True, null=True)
    answerLocationType = models.TextField(default=None, blank=True, null=True)
    scriptureBookName = models.TextField(default=None, blank=True, null=True)
    scriptureChapterNumber = models.IntegerField(default=None, blank=True, null=True)
    scriptureVerseNumber = models.IntegerField(default=None, blank=True, null=True)
    handoutCharacterStart = models.IntegerField(default=None, blank=True, null=True)
    handoutCharacterEnd = models.IntegerField(default=None, blank=True, null=True)

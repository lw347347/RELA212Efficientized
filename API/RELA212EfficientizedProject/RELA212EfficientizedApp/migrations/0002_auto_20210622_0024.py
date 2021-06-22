# Generated by Django 3.2.4 on 2021-06-22 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RELA212EfficientizedApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='questionNumber',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='questiongroup',
            name='questionGroupNumber',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='studyguide',
            name='studyGuideNumber',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='answerText',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='questionId',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='RELA212EfficientizedApp.question'),
        ),
        migrations.AlterField(
            model_name='answerhint',
            name='answerHintType',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='answerhint',
            name='handoutCharacterEnd',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='answerhint',
            name='handoutCharacterStart',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='answerhint',
            name='questionId',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='RELA212EfficientizedApp.question'),
        ),
        migrations.AlterField(
            model_name='answerhint',
            name='scriptureBookName',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='answerhint',
            name='scriptureChapterNumber',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='answerhint',
            name='scriptureVerseNumber',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='answerlocation',
            name='answerId',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='RELA212EfficientizedApp.answer'),
        ),
        migrations.AlterField(
            model_name='answerlocation',
            name='answerLocationType',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='answerlocation',
            name='handoutCharacterEnd',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='answerlocation',
            name='handoutCharacterStart',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='answerlocation',
            name='scriptureBookName',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='answerlocation',
            name='scriptureChapterNumber',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='answerlocation',
            name='scriptureVerseNumber',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='examEndDate',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='examNumber',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='examStartDate',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='questionGroupId',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='RELA212EfficientizedApp.questiongroup'),
        ),
        migrations.AlterField(
            model_name='question',
            name='questionText',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='questiongroup',
            name='countOfQuestions',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='questiongroup',
            name='scriptureBookName',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='questiongroup',
            name='scriptureChapterNumber',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='questiongroup',
            name='studyGuideId',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='RELA212EfficientizedApp.studyguide'),
        ),
        migrations.AlterField(
            model_name='studyguide',
            name='dateOfAssignment',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='studyguide',
            name='examId',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='RELA212EfficientizedApp.exam'),
        ),
        migrations.AlterField(
            model_name='studyguide',
            name='file',
            field=models.BinaryField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='studyguide',
            name='name',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='studyguide',
            name='typeOfStudyGuide',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]

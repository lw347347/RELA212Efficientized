# Generated by Django 3.1.3 on 2021-06-27 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RELA212EfficientizedApp', '0004_auto_20210626_0310'),
    ]

    operations = [
        migrations.AddField(
            model_name='studyguide',
            name='questionGroupBeginning',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='studyguide',
            name='questionGroupSplitter',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
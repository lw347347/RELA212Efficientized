from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'exams', views.ExamsViewSet)
router.register(r'studyGuides', views.StudyGuidesViewSet)
router.register(r'questionGroups', views.QuestionGroupsViewSet)
router.register(r'questions', views.QuestionsViewSet)
router.register(r'qnswerHints', views.AnswerHintsViewSet)
router.register(r'answers', views.AnswersViewSet)
router.register(r'answerLocations', views.AnswerLocationsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
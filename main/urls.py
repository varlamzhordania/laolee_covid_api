from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import CovidCaseViewSet

app_name = 'main'

router = SimpleRouter()
router.register(r"covid", CovidCaseViewSet)


urlpatterns = []
urlpatterns += router.urls

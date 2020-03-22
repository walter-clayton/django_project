from rest_framework import routers
from chart.viewsets import ChartViewSet

router = routers.DefaultRouter()
router.register(r'chart', ChartViewSet)
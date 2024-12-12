from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserAccountViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CustomTokenObtainPairView, AnalyticsSummaryView

router = DefaultRouter()
router.register('users', UserAccountViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('analytics/summary/', AnalyticsSummaryView.as_view(), name='analytics-summary'),
]

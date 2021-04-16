from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from .views import MyTokenObtainPairView, RessourceViewSet, UserViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'users', UserViewSet)
router.register(r'ressources', RessourceViewSet)
urlpatterns = router.urls

#add specific nested routes
urlpatterns += [
    path('ressources/<str:share_id>/bookings/<int:booking>', RessourceViewSet.as_view({
                                                                'patch': 'booking_patch',
                                                                'delete': 'booking_delete'})),
    # AUTH JWT
    path('auth/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

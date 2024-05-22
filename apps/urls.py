from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.views import CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView, ProductModelViewSet
from rest_framework.authtoken import views

router = DefaultRouter()
router.register('product', ProductModelViewSet, 'product')

urlpatterns = [
    path('category/', CategoryListCreateAPIView.as_view()),
    path('category/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('', include(router.urls)),
    # path('api-token-auth/', views.obtain_auth_token)
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('product/', ProductListCreateAPIView.as_view()),
    # path('product/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view()),
]


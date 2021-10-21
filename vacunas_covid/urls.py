from django.contrib                 import admin
from django.urls                    import path
from rest_framework_simplejwt.views import(TokenObtainPairView, TokenRefreshView)
from asignacion_vacunas             import views as authAppViews

urlpatterns = [
    path('admin/',                                 admin.site.url),
    path('login/',                                 TokenObtainPairView.as_view()),
    path('refresh/',                               TokenRefreshView.as_view()),    
    path('territorio/',                            authAppViews.TerritorioCreateView.as_view()),
    path('territorio/<int:pk>/',                   authAppViews.TerritorioDetailView.as_view()),
    path('asignacion/',                            views.asignacionCreateView.as_view()),
    path('asignacion/<int:user>/',                 views.asignacionUserView.as_view()),
    path('asignacion/remove/<int:user>/<int:pk>/', views.asignacionDeleteView.as_view()),
    path('asignacion/update/<int:user>/<int:pk>/', views.asignacionUpdateView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,  document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

]
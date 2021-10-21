from django.contrib                 import admin
from django.urls                    import path, include 
from rest_framework_simplejwt.views import(TokenObtainPairView, TokenRefreshView)
from asignacion_vacunas             import views as authAppViews
from django.conf.urls.static        import static
from django.conf                    import settings

urlpatterns = [
    path('admin/',                                 admin.site.urls),
    path('login/',                                 TokenObtainPairView.as_view()),
    path('refresh/',                               TokenRefreshView.as_view()),    
    path('territorio/',                            authAppViews.TerritorioCreateView.as_view()),
    path('territorio/<int:pk>/',                   authAppViews.TerritorioDetailView.as_view()),
    path('asignacion/',                            authAppViews.AsignacionCreateView.as_view()),
    path('asignacion/<int:user>/',                 authAppViews.AsignacionTerritorioView.as_view()),
    path('asignacion/remove/<int:user>/<int:pk>/', authAppViews.AsignacionDeleteView.as_view()),
    path('asignacion/update/<int:user>/<int:pk>/', authAppViews.AsignacionUpdateView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,  document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
from django.contrib                 import admin
from django.urls                    import path
from rest_framework_simplejwt.views import(TokenObtainPairView, TokenRefreshView)
from asignacion_vacunas             import views as authAppViews

urlpatterns = [
    path('admin/',                                 admin.site.urls),
    path('refresh/',                               TokenRefreshView.as_view()),
    path('asignacion/',                            authAppViews.AsignacionDetailView.as_view()),
    path('vacuna/create/',                         authAppViews.VacunaCreateView.as_view()),
    path('vacuna/<int:user>/<int:pk>/',            authAppViews.VacunaDetailView.as_view()), 
    path('vacuna/update/<int:user>/<int:pk>/',     authAppViews.VacunaUpdateView.as_view()),
    path('vacuna/remove/<int:user>/<int:pk>/',     authAppViews.VacunaDeleteView.as_view()),
    path('vacuna/<int:user>/<int:account>/',       authAppViews.VacunaAsignacionView.as_view()),
    path('territorio/create/',                     authAppViews.TerritorioCreateView.as_view()),
    path('territorio/<int:user>/<int:pk>/',        authAppViews.TerritorioDetailView.as_view()),
    path('territorio/<int:user>/<int:account>/',   authAppViews.TerritorioAsignacionView.as_view()),
    path('territorio/update/<int:user>/<int:pk>/', authAppViews.TerritorioUpdateView.as_view()),
    path('territorio/remove/<int:user>/<int:pk>/', authAppViews.TerritorioDeleteView.as_view()),
]
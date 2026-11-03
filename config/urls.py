from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from dojoApp.views import dashboard_view

urlpatterns = [
    # Panel Admin de Django
    path('admin/', admin.site.urls),
    
    # Ruta principal
    path('', dashboard_view, name='home'),
    
    # Rutas de Autenticación
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    
    # --- NUEVO: Flujo de Recuperación de Contraseña (Día 5) ---
    path('reset_password/', 
        auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"), 
        name="reset_password"),
    
    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), 
        name="password_reset_done"),
    
    path('reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), 
        name="password_reset_confirm"),
    
    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), 
        name="password_reset_complete"),
    
    # Rutas internas de las aplicaciones
    path('alumnos/', include('dojoApp.urls')),
    path('eventos/', include('eventosApp.urls')),
]
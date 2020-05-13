from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as authViews
urlpatterns = [
    path('pass-reset/',authViews.PasswordResetView.as_view(template_name='pass_reset.html'),
         name='pass-reset'),

    path('password_reset_confirm/<uidb64>/<token>/',authViews.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset_complete/',authViews.PasswordResetCompleteView.as_view(template_name='password-reset_complete.html'),
         name='password-reset_complete'),

    path('password-reset/done/',authViews.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('admin/', admin.site.urls),
    path('',include('shop.urls')),
    path('auth/',include('users.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()

from django.contrib import admin
from django.urls import path, include
from painel import urls as painel_urls
from home import urls as home_urls
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar
from django.contrib.auth import views as auth_views

from rest_framework import routers
from .views import UserViewSet, GroupViewSet

from painel.views import ContatoViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'contato', ContatoViewSet)



#TODO: Retirar todas as configurações de exibições de arquivos staticos de media da raiz do projeto!
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('painel/', include(painel_urls)),
    path('', include(home_urls)),
    path('__debug__/', include(debug_toolbar.urls)),
    path('rest-api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'PTC-System'     
admin.site.index_title = 'PTC-System'
admin.site.site_title = 'PTC-Protocol System'
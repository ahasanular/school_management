from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from settings.views import FooterInfo
from signin.views import SignInApi


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('students/', include('students.urls')),
    path('teachers/', include('teachers.urls')),
    path('facilities/', include('facilities.urls')),
    path('posts/', include('posts.urls')),
    path('settings/', include('settings.urls')),
    path('contacts/', include('contacts.urls')),

    #signin/signup/verification
    path('sign_up/', include('signup.urls')),
    path('sign_in/', include('signin.urls')),
    # path('', include('signin.urls')),

    #api
    path('sign_in_api/', SignInApi.as_view()),


    #Footer api
    path('footer_info_api/', FooterInfo.as_view()),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

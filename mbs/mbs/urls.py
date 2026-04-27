from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from bms.views import books, delete_book, update_book, login_page, logout_page, register_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', books, name="books"),

    path('login/', login_page, name='login_page'),
    path('register/', register_page, name='register_page'),  
    path('logout/', logout_page, name='logout_page'),         

    path('delete_book/<int:id>/', delete_book, name='delete_book'),
    path('update_book/<int:id>/', update_book, name='update_book'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path
from birds import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('birds/add/', views.bird_create, name='bird_create'),
    path('birds/<int:bird_id>/edit/', views.bird_edit, name='bird_edit'),
    path('birds/<int:bird_id>/delete/', views.bird_delete, name='bird_delete'),

    path('birds/<int:bird_id>/', views.bird_detail, name='bird_detail'),

    # 体重記録追加・編集・削除ページ
    path('birds/<int:bird_id>/add-weight/', views.add_weight, name='add_weight'),
    path('weights/<int:weight_id>/edit/', views.edit_weight, name='edit_weight'),
    path('weights/<int:weight_id>/delete/', views.delete_weight, name='delete_weight'),

    # 行動記録追加・編集・削除ページ
    path('birds/<int:bird_id>/add-behavior/',views.add_behavior,name='add_behavior'),
    path('behaviors/<int:behavior_id>/edit/',views.edit_behavior,name='edit_behavior',),
    path('behaviors/<int:behavior_id>/delete/',views.delete_behavior,name='delete_behavior'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
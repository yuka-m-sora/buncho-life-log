from django.contrib import admin
from django.urls import path
from birds import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
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
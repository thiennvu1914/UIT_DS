from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.Home, name='home'),
    
    path("", views.custom_login, name="custom_login"),
    path('logout', views.logout_user, name='logout'),
    
    path('ban/', views.ban_view, name='ban_view'),
    path('ban/search/', views.search_ban_view, name='search_ban_view'),
    path('ban/add/', views.add_ban, name='add_ban'),
    path('ban/edit/<int:ban_id>/', views.edit_ban, name='edit_ban'),
    path('ban/delete/<int:ban_id>/', views.delete_ban, name='delete_ban'),
    
    path('ban/<int:ban_id>/order_detail/', views.order_detail_view, name='order_detail'),
    path('ban/<int:ban_id>/add/customer/', views.add_menu_item_customer, name='add_menu_item_customer'),
    path('ban/<int:ban_id>/add/', views.add_menu_item_to_order, name='add_menu_item_to_order'),
    path('ban/<int:ban_id>/delete/<int:item_id>/', views.delete_order_item, name='delete_order_item'),
    path('ban/<int:order_id>/update_customer/', views.update_order_customer, name='update_order_customer'),
    path('ban/order_detail/<int:order_id>/thanh_toan/', views.thanh_toan, name='thanh_toan'),
    path('update-tinhtrang/<int:chi_tiet_order_id>/', views.update_tinhtrang, name='update_tinhtrang'),
    
    path('employees/', views.all_employees, name='all_employees'),
    path('employees/search/', views.search_nhanvien_view, name='search_nhanvien_view'),
    path("employees/add/", views.add_employee, name="add_employee"),
    path("employees/edit/<int:pk>/", views.edit_employee, name="edit_employee"),
    path("employees/delete/<int:pk>/", views.delete_employee, name="delete_employee"),
    path('employees/<int:employee_id>/shifts/', views.calamviec_nv, name='calamviec_nv'),
   
    path('menu/', views.menu_view, name='menu'),
    path('menu/search/', views.search_menu_view, name='search_menu_view'),
    path('menu/add/', views.add_menu_view, name='add_menu_view'),  
    path('menu/edit/<int:menu_id>/', views.edit_menu_view, name='edit_menu_view'),  
    path('menu/delete/<int:menu_id>/', views.delete_menu_view, name='delete_menu_view'), 
    
    path('doanhthu', views.order_view, name='order_view'),
    path('doanhthu/search/', views.search_order_detail_dapaid, name='search_order_detail_dapaid'),
    path('doanhthu/<int:order_id>/', views.order_detail_dapaid, name='order_detail_dapaid'),
    
    path('calamviec/', views.calamviec, name='calamviec'),
    path('calamviec/add/', views.them_ca_lam_viec, name='them_ca_lam_viec'),
    path('calamviec/edit/<int:pk>/', views.sua_ca_lam_viec, name='sua_ca_lam_viec'),
    path('calamviec/delete/<int:pk>/', views.xoa_ca_lam_viec, name='xoa_ca_lam_viec'),
    path('calamviec/checkin/<int:id>/', views.cham_cong_vao, name='cham_cong_vao'),
    path('calamviec/checkout/<int:id>/', views.cham_cong_ra, name='cham_cong_ra'),
    path('calamviec/nhanvientrongca/', views.nhanvientrongca, name='nhanvientrongca'),

    path('khuyenmai/', views.khuyenmai_view, name='khuyenmai'),
    path('khuyenmai/add/', views.add_khuyenmai_view, name='add_khuyenmai'),
    path('khuyenmai/edit/<int:km_id>/', views.edit_khuyenmai_view, name='edit_khuyenmai'),
    path('khuyenmai/delete/<int:km_id>/', views.delete_khuyenmai_view, name='delete_khuyenmai'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

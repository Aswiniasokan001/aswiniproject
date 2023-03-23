from django.urls import path
from . import views

urlpatterns = [

		path('',views.index),
		path('about/',views.about),
		path('services/',views.services),
		path('single/',views.single),
		path('team_single/',views.team_single),
		path('login/',views.login),
		# path('timeline/',views.timeline),
		# path('faq/',views.faq),
		path('contact/',views.contact),
		path('portfolio/',views.portfolio),
		path('condact_display/',views.condact_display),
		# path('condact_delete/',views.condact_delete),

		# path('services/',views.services),
		
		########################################ADMIN##################################

		path('admin_index/',views.admin_index),
		path('admin_forms/',views.admin_forms),
		path('admin_cards/',views.admin_forms),
		path('admin_pricing/',views.admin_pricing),
		path('admin_login/',views.admin_login),
		path('admin_register/',views.admin_register),
		path('admin_logout/',views.admin_logout),
		path('admin_product/',views.admin_product),
		path('product_display/',views.product_display),
		path('product_delete/',views.product_delete),
		path('update_product/',views.update_product),
		path('image_enter/',views.image_enter),
		path('image_display/',views.image_display),


]


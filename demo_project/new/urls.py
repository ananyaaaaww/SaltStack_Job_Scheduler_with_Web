# urls.py
from django.urls import path
from . import views
from django.conf import settings  # Import settings
from django.conf.urls.static import static 

urlpatterns = [ 
    path('home/', views.home_form_view),
    path('home/delete.html',views.delete_form_view),
    path('home/enable.html',views.enable_form_view),
    path('home/disable.html',views.disable_form_view),
    path('home/job_status.html',views.status_form_view),
    path('home/run_job.html',views.runjob_form_view),
    path('home/purge.html',views.purge_form_view),
    path('home/reload.html',views.reload_form_view),
    path('home/list.html',views.list_form_view),
    path('home/add.html',views.add_form_view),
    path('home/modify.html',views.modify_form_view),
    path('salt/function/', views.SaltFunctionView.as_view(), name='salt_function')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


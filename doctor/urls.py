from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index, name="DocHome"),
    path('pat',views.patients, name="DocList"),
    path('checkup/<int:id>',views.checkup, name="DocCheck"),
    path('save/<int:id>',views.save, name="DocSave"),
    path('prev_rec/<int:id>',views.prev_rec, name="DocPrevRec"),
]
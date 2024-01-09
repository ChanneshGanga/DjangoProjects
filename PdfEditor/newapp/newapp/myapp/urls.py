# myapp/urls.py
from django import views
from django.urls import path
from .views import delete, save_changes_view, update_pdf_file, upload, list, view_document, view_pdf

urlpatterns = [
    path('upload/', upload, name='upload_document'),
    path('documents/', list, name='document_list'),
    path('textdocuments/<int:id>/', view_document, name='view_document'),
    path('delete/', delete, name='delete'),
    path('view/<int:pdf_id>/', view_pdf, name='view_pdf'),
    path('save_changes/', save_changes_view, name='save_changes'),
    path('update_pdf_file/<int:pdf_id>/', update_pdf_file, name='update_pdf_file'),
]


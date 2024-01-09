from django import forms
from .models import Document, PDF

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('name', 'document',)

class PDFDocumentForm(forms.ModelForm):
    class Meta:
        model = PDF
        fields = ('title', 'pdf')
from django.db import models

class Document(models.Model):
    document_id = models.AutoField
    name = models.CharField(max_length=25, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class PDF(models.Model):
    pdf_id = models.AutoField
    title = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
import json
import os
from django.http import FileResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PDFDocumentForm
from .models import Document, PDF
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse

def list(request):
    documents = Document.objects.all()
    pdfdocuments = PDF.objects.all()
    return render(request, 'list.html', {'documents': documents, 'pdfdocuments': pdfdocuments})

def upload(request):
    if request.method == 'POST':
        if 'document' in request.FILES:
            # This is for the text document form
            document = request.FILES['document']
            name = request.POST['name']
            Document.objects.create(document=document, name=name)
            messages.success(request, 'Text document uploaded successfully')
        elif 'pdfdocument' in request.FILES:
            # This is for the PDF document form
            document = request.FILES['pdfdocument']
            name = request.POST['pdfname']
            PDF.objects.create(pdf=document, title=name)
            messages.success(request, 'PDF document uploaded successfully')
    return render(request, 'upload.html')

def delete(request):
    if request.method == 'POST':
        document_id = request.POST.get('document_id')
        pdf_id = request.POST.get('pdf_id')

        try:
            if document_id:
                document = Document.objects.get(id=document_id)
                document.delete()
                messages.success(request, 'Text document deleted successfully')
            elif pdf_id:
                pdf = PDF.objects.get(id=pdf_id)
                pdf.delete()
                messages.success(request, 'PDF document deleted successfully')
        except (Document.DoesNotExist, PDF.DoesNotExist):
            messages.error(request, 'Failed to delete the document')

    return redirect('/myapp/documents')

# def view_pdfdocument(request, id):
#     document = PDF.objects.filter(id = id)[0]
#     pdf_path = document.pdf.path
#     return render(request, 'docview.html', {'pdf_path': pdf_path,'document':document})

def view_document(request, id):
    try:
        pdf = Document.objects.get(pk=id)
        return render(request, 'docview.html', {'pdf': pdf})
    except PDF.DoesNotExist:
        return HttpResponse("PDF not found", status=404)

# def view(request):
#     document = Document.objects.first
#     # pdf_path = document.document.path
#     return render (request, 'docview.html')

# def view_pdf_page(request, path):
#     # You can render an HTML template that includes a PDF viewer here
#     return render(request, 'docview.html', {'pdf_path': path})

# def view_pdf(request, path):
#     file_path = os.path.join(settings.MEDIA_ROOT, path)
#     if os.path.exists(file_path):
#         return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
#     else:
#         return HttpResponse("PDF not found")
    
def view_pdf(request, pdf_id):
    try:
        pdf = PDF.objects.get(pk=pdf_id)
        return render(request, 'docview.html', {'pdf': pdf})
    except PDF.DoesNotExist:
        return HttpResponse("PDF not found", status=404)
    
def update_pdf_file(request, pdf_id):
    print('updating pdf id', pdf_id)
    media_file = get_object_or_404(PDF, pk=pdf_id)
    print(media_file)
    if request.method == 'POST':
        print(request.FILES)
        form = PDFDocumentForm(request.POST, request.FILES, instance=media_file)
        if form.is_valid():
            print('PDF is valid')
            form.save()
            return JsonResponse({'message': 'Media file updated successfully'}, status=200)
        else:
            print('PDF is not valid')
            return JsonResponse({'error': 'Invalid form data'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


def save_changes_view(request):
    if request.method == 'POST':
        try:
            # Get JSON data from the request body
            data = json.loads(request.body.decode('utf-8'))

            # Process and save the changes (replace this with your actual logic)
            # For now, let's just print the changes
            print("Received changes:", data)

            # Return a JsonResponse to indicate success (replace this with your actual response)
            return JsonResponse({'status': 'success'})
        except json.JSONDecodeError as e:
            # Return an error response if JSON decoding fails
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON format'})
    else:
        # Return an error response for non-POST requests
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
from django.shortcuts import render
from django.http import HttpResponse
import io
from PyPDF2 import PdfFileMerger
def input(request):
    if request.method=='POST':
        pdf1=request.FILES['pdf1']
        pdf2=request.FILES['pdf2']
        merger=PdfFileMerger()
        merger.append(pdf1)
        merger.append(pdf2)
        mergeed_pdf=io.BytesIO()
        merger.write(mergeed_pdf)
        return HttpResponse(mergeed_pdf.getvalue(),content_type='application/pdf')
    return render(request,'input.html')
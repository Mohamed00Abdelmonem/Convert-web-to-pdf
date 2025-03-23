from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
import pdfkit
from .forms import MyForm
from .models import FlightItinerary

# Path to wkhtmltopdf executable
wkhtmltopdf_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # Update this path

# Configure pdfkit
pdfkit_config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

def home(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_data')
    else:
        form = MyForm()
    return render(request, 'index.html', {'form': form})

def display_data(request):
    data = FlightItinerary.objects.last()  # Get the latest entry
    return render(request, 'display_data.html', {'data': data})

def download_pdf(request):
    data = FlightItinerary.objects.last()
    html = render_to_string('display_data.html', {'data': data})
    pdf = pdfkit.from_string(html, False, configuration=pdfkit_config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="data.pdf"'
    return response
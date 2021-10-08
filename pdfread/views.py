from django.shortcuts import render
import pdfplumber

def plum_dadal(filename):
    text = ""
    with pdfplumber.open(filename) as pdf:
        for i in range(len(pdf.pages)):
            page = pdf.pages[i]
            text += page.extract_text()
    return text

# Create your views here.
def index(request):
    context = {}
    if request.method=="POST":
        
        pdf = request.FILES.get("pdf")
        context.update ({
            "con" : plum_dadal(pdf)
        })


        plum_dadal(pdf)

    return render(request,"pdfread/index.html",context)
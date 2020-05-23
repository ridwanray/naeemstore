from django.shortcuts import render


def home(request):
    
    return render(request, 'home.html', {"title":"Annaeem Store | Islamic Store |"})

def about(request):
    return render(request, 'about.html', {"title":"About Us | Annaeem Store"})

def contact(request):
    return render(request, 'contact.html', {"title":"Contact Us | Annaeem Store"})

def faqs(request):
    return render(request, 'faqs.html', {"title":"FAQs | Annaeem Store Questions&Answers"})
def enquiry(request):
    return render(request, 'enquiry.html', {"title":"Enquiry | Annaeem Store"})
def category(request):
    return render(request, 'category.html', {"title":"Category | Annaeem Store"})
def review(request):
    return render(request, 'review.html', {"title":"Reviews | Annaeem Store"})
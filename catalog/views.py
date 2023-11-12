from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'catalog/homepage.html')

def contact_information(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name, message, email)
    return render(request, 'catalog/contact_information.html')
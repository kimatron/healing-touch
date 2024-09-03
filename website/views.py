from django.shortcuts import render


def home(request):
    return render(request, 'website/home.html')


def services(request):
    return render(request, 'website/services.html')


def about(request):
    return render(request, 'website/about.html')


def gallery(request):
    return render(request, 'website/gallery.html')


def booking(request):
    return render(request, 'website/booking.html')

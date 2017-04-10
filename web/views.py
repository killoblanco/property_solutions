from django.shortcuts import render


# Create your views here.
def landing_single_view(request):
    return render(request, 'web/pages/landing_single_view.html')

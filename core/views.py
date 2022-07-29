from django.shortcuts import render


# Create your views here.
def price_view(request):
    return render(request, "core/price.html")


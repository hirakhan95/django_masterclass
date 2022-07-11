from django.http.response import HttpResponse


def home_view(request):
    name = "HIRA"
    return HttpResponse(f"Welcome {name}!!")
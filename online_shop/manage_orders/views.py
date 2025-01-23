from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def search_item(request):

    return render(request, "search_item.html")

def search(request):

    message: str = ""

    if request.GET["itm"]:
        message = f"Searched item: '{request.GET["itm"]}'"

        if len(request.GET["itm"]) > 20:
            message = "The searched item is too long"
    else:
        message = "Empty search"

    return HttpResponse(message)
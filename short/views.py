from django.shortcuts import render, redirect
import uuid
from short.models import Url
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

# Create your views here.

def  head(req):
    return render(req,'head.html')   
def create(req):
    if req.method == 'POST':
        link= req.POST['link']
        uid= str(uuid.uuid4())[:5]
        new_url= Url(link=link,uuid=uid)
        new_url.save()
        return HttpResponse(uid)
    
def go(req, pk):
    url_details =Url.objects.get(uuid=pk)
    if 'http' in url_details.link:
        return redirect(url_details.link)
    return redirect('https://'+url_details.link)

@require_http_methods(["GET"])
def favicon_view(request):
    # Serve your favicon file here, or return a placeholder response
    # In a real application, you would return an actual favicon.ico file
    return HttpResponse(status=204)  # Placeholder response

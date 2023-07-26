from rest_framework import status,generics
from rest_framework.views import APIView
from django.http import HttpResponsePermanentRedirect

from .models import Link
from .serializers import LinkSerializers

# Create your views here.

class ShortenUrl(generics.CreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer



def redirect_to_long_url(self,request,short_identifier):
    url = get_object_or_404(Link, shorten_url=short_identifier)
    return HttpResponsePermanentRedirect(url.target_url) 
        



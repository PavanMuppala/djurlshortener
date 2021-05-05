from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from .models import UrlShort
from .serializers import UrlShortSerializer


class UrlShortViewSet(ModelViewSet):

    queryset = UrlShort.objects.all()
    serializer_class = UrlShortSerializer


def url_redirect(request, url):

    data = UrlShort.objects.get(short_url=url)
    url_data = {
        "success": True,
        "id": data.pk,
        "short_url": data.short_url,
        "long_url": data.url
    }
    return JsonResponse(url_data)

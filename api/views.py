from django.shortcuts import get_object_or_404, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Url
from .serializers import UrlSerializer


class UrlView(APIView):
    def get(self, request, short_url=None):
        if short_url:
            url = get_object_or_404(Url, short_url=short_url)
            f_url = url.full_url
            url.counter += 1
            url.save()
            return redirect(f_url)
        # List all URLs if no short_url is provided
        urls = Url.objects.all()
        serializer = UrlSerializer(urls, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UrlSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the validated data to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

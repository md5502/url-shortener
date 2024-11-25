from django.shortcuts import get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST

from .models import Url
from .serializers import UrlSerializerIn, UrlSerializerOut
from .utils import delete_cache, get_cached_url, set_cached_url, update_cache


@api_view(["get"])
def list_url(request):
    data = Url.objects.all()

    data = UrlSerializerOut(data, many=True).data

    return Response(data)



@api_view(["POST"])
def create_url(request):
    url_data = request.data.get("url")
    if not url_data:
        return Response({"msg": "URL field is required."}, status=HTTP_400_BAD_REQUEST)

    serializer = UrlSerializerIn(data={"url": url_data})
    if serializer.is_valid():
        obj = Url.objects.create(url=url_data)
        # Save URL to cache
        set_cached_url(obj.short_code, obj.url, obj.access_count)

        response_data = UrlSerializerOut(obj).data
        return Response(response_data, status=HTTP_201_CREATED)

    return Response(
        {"msg": "Validation error", "errors": serializer.errors},
        status=HTTP_400_BAD_REQUEST,
    )


@api_view(["PUT"])
def update_url(request, short_code):
    obj = get_object_or_404(Url, short_code=short_code)

    url = request.data.get("url")
    if not url :
        return Response({"msg": "URL field is required."}, status=HTTP_400_BAD_REQUEST)

    serializer = UrlSerializerIn(data={"url": url})
    if serializer.is_valid():
        obj.url = serializer.data.get("url")
        update_cache(short_code, obj.url)
        obj.save()

        response_data = UrlSerializerOut(obj).data
        return Response(response_data, status=HTTP_200_OK)

    return Response(
        {
            "msg": "Validation error",
            "errors": serializer.errors,
        },
        status=HTTP_400_BAD_REQUEST,
    )

@api_view(["DELETE"])
def delete_url(request, short_code):
    obj = get_object_or_404(Url, short_code=short_code)
    obj.delete()
    delete_cache(short_code)
    return Response(
        {
            "msg": f"url with the {short_code} deleted successfully",
        },
        status=HTTP_204_NO_CONTENT,
    )



@api_view(["GET"])
def retrieve_url(request, short_code):
    url = get_object_or_404(Url, short_code=short_code)
    serializer = UrlSerializerOut(url)
    return Response(data=serializer.data, status=HTTP_200_OK)



@api_view(["GET"])
def go_to_base_url(request, short_code):
    url = get_cached_url(short_code)
    if url:
        return redirect(url)
    obj = get_object_or_404(Url, short_code=short_code)
    set_cached_url(obj.short_code, obj.url, obj.access_count)
    return redirect(obj.url)

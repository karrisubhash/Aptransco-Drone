import os

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ImageUploadSerializer

from .services.yolo26_detector import run_detection


@api_view(['POST'])
def detect_defects(request):

    serializer = ImageUploadSerializer(
        data=request.data
    )

    if serializer.is_valid():

        image = serializer.validated_data['image']

        image_path = os.path.join(
            "media/uploads",
            image.name
        )

        with open(image_path, 'wb+') as destination:

            for chunk in image.chunks():
                destination.write(chunk)

        results = run_detection(image_path)

        return Response({
            "status": "success",
            "results": results
        })

    return Response(serializer.errors)
from rest_framework import status, views
from rest_framework.response import Response


class StatusView(views.APIView):
    authentication_classes = []
    serializer_class = None

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Note
from .serializers import NoteSerializer


class NoteView(APIView):
    def get(self, request):
        Notes = Note.objects.all()
        # the many param informs the serializer that it will be serializing more than a single Note.
        serializer = NoteSerializer(Notes, many=True)
        return Response({"Notes": serializer.data})

    def post(self, request):
        Note = request.data.get('Note')
        # Create an Note from the above data
        serializer = NoteSerializer(data=Note)
        if serializer.is_valid(raise_exception=True):
            Note_saved = serializer.save()
        return Response({"success": "Note '{}' created successfully".format(Note_saved.title)})

    def put(self, request, pk):
        saved_Note = get_object_or_404(Note.objects.all(), pk=pk)
        data = request.data.get('Note')
        serializer = NoteSerializer(instance=saved_Note, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            Note_saved = serializer.save()
        return Response({
            "success": "Note '{}' updated successfully".format(Note_saved.title)
        })

    def delete(self, request, pk):
        # Get object with this pk
        Note = get_object_or_404(Note.objects.all(), pk=pk)
        Note.delete()
        return Response({
            "message": "Note with id `{}` has been deleted.".format(pk)
        }, status=204)

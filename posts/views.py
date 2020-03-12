from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework import viewsets
from reportlab.pdfgen import canvas
from django.http import HttpResponse


from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly

from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse

# def some_view(request):
#     # Create the HttpResponse object with the appropriate PDF headers.
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

#     # Create the PDF object, using the response object as its "file."
#     p = canvas.Canvas(response)

#     # Draw things on the PDF. Here's where the PDF generation happens.
#     # See the ReportLab documentation for the full list of functionality.
#     p.drawString(100, 100, "Hello world.")

#     # Close the PDF object cleanly, and we're done.
#     p.showPage()
#     p.save()
#     return response




class PostListCreate(generics.ListCreateAPIView):
  """Post list and create api view."""
  # permission_class = (permissions.IsAuthenticated)
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
  """Post retrieve update and destroy api view."""
  # permission_classes = (IsAuthorOrReadOnly,)
  queryset = Post.objects.all()
  serializer_class = PostSerializer


class UserList(generics.ListCreateAPIView): 
  queryset = get_user_model().objects.all()
  serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateAPIView):
  queryset = get_user_model().objects.all()
  serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet): # new
  permission_classes = (IsAuthorOrReadOnly,)
  queryset = Post.objects.all()
  serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
  """Use viewsets for user create, update, list, retrive"""
  queryset = get_user_model().objects.all()
  serializer_class = UserSerializer



def some_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    buffer = BytesIO()

    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    q = Post.objects.all()
    for i in q:
      print(i.title)
      p.drawString(100, 100, i.title)

    # Close the PDF object cleanly.
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response


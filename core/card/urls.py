from django.urls import path
from .views import CreateFlashCardView,UpdateFlashCardView,DeleteFlashCardView,ListFlashCardView


urlpatterns = [
    path('create/', CreateFlashCardView.as_view(), name="create-flashcard"),
    path('update/<id>/', UpdateFlashCardView.as_view(), name="update-flashcard"),
    path('delete/<id>/', DeleteFlashCardView.as_view(), name="delete-flashcard"),
    path('list/<user_id>/', ListFlashCardView.as_view(), name="list-flashcard"),
]
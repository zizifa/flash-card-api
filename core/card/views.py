from rest_framework.views import APIView
from .serializer import CreateFlashCardSerialize,UpdateFlashCardSerialize,ListFlashCardSerialize
from rest_framework.response import Response
from .models import FlashCard
from django.shortcuts import get_object_or_404,get_list_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class CreateFlashCardView(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self,request):
        serializer=CreateFlashCardSerialize(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data,status=status.HTTP_201_CREATED)


class UpdateFlashCardView(APIView):

    permission_classes = (IsAuthenticated,)

    def put(self,request,id):
        req_data=request.data
        data_obj=get_object_or_404(FlashCard,id=id)
        serializer=UpdateFlashCardSerialize(data=req_data,instance=data_obj)
        serializer.is_valid()
        serializer.save()

        return Response(serializer.data,status=status.HTTP_200_OK)

class DeleteFlashCardView(APIView):

    permission_classes = (IsAuthenticated,)

    def delete(self,request,id):
        data_obj=get_object_or_404(FlashCard,id=id)
        data_obj.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ListFlashCardView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self,request,user_id):

        user_cards = get_list_or_404(FlashCard, user__id=user_id) #get_object_or_404 take just one obj but get_list_or_404 take a list
        serializer=ListFlashCardSerialize(
            user_cards,
            many=True,
        )
        return Response(serializer.data)
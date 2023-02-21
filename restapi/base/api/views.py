from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CallLogSerializer
from django.db.models import Q
from base.models import CallLog
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 10
    

@api_view(['POST'])
def initiateCall(request):
    print(request.data)
    callData = CallLogSerializer(data = request.data)
    if callData.is_valid():
        callData.save()
        return Response(callData.data, status=status.HTTP_201_CREATED)
    else:
        return Response(callData.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def getData_with_number(request):
   number = request.GET.get('phone')
   print(number)
   paginator = CustomPagination()
   queryset = CallLog.objects.filter(Q(from_number=number) |Q(to_number=number)) 
   result_page = paginator.paginate_queryset(queryset, request)
   serializer = CallLogSerializer(result_page, many=True)
   return paginator.get_paginated_response(serializer.data)

@api_view(['PUT'])
def update_callLog(request,pk):
    
    try:
        call = CallLog.objects.get(id=pk)
    except CallLog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CallLogSerializer(call, data=request.data)
    if serializer.is_valid():
        
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_callLog(request,pk):
    try:
        data = CallLog.objects.get(id=pk)
    except CallLog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data.delete()
    return  Response(status=status.HTTP_200_OK)
    
    
   

   
   
   
   


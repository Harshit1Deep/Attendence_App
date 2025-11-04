
from .models import Attendence
from rest_framework.views import APIView 
from rest_framework import status
from rest_framework.response import Response


class Sheet(APIView):
    def post(self,request):
        name = request.data.get("name")
        roll = request.data.get("roll")
        attendence = request.data.get("attendence")
        date = request.data.get("date")

        if name and roll and attendence and date:
            sheet = Attendence.objects.create(
                name= name,roll=roll,attendence=attendence,date = date
            )
            return Response({"status":"success","message":"Data saved successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response({"status":"error","message":"Field required"},status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self,request):
        print(request.data)
        sheets = Attendence.objects.all().values('slno','name','roll','attendence','date')
        sheet_list = list(sheets)
        return Response({"status":"success","data":sheet_list},status=status.HTTP_200_OK)
    
    def patch(self,request):
        sheetid = request.data.get('slno')
        if not sheetid:
            return Response({
                "status":"error","message":"ID is required for update"
            },status=status.HTTP_400_BAD_REQUEST)
        try:
            sheet = Attendence.objects.get(slno = sheetid)
        except Attendence.DoesNotExist:
            return Response({
                "status":"error","message":"record not found"
            },status=status.HTTP_404_NOT_FOUND)    
        
        name = request.data.get("name")
        roll = request.data.get("roll")
        attendence = request.data.get("attendence")
        date = request.data.get("date")
        if name:
            sheet.name = name
        if roll:
            sheet.roll = roll
        if attendence:
            sheet.attendence = attendence
        if date:
            sheet.date = date
        sheet.save()
        return Response({
            "status":"success","message":"record updated successfully"
        },status=status.HTTP_200_OK)                
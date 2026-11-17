from django.shortcuts import render,get_object_or_404

# Create your views here.
from rest_framework.views import APIView

from rest_framework import authentication,permissions


from rest_framework.response import Response


from transactions.models import Expense

from transactions.serializers import ExpenseSerializer




class ExpenselisteCreateView(APIView):

    authentication_classes=[authentication.BasicAuthentication]

    parser_classes=[permissions.IsAuthenticated]

    def get(self,request):

        auth_user=request.user

        qs=Expense.objects.filter(owner=auth_user)

        serializer_instance=ExpenseSerializer(qs,many=True)

        return Response(serializer_instance.data)

    def post(self,request):

        from_data=request.data

        auth_user=request.user

        serializer_instance=ExpenseSerializer(data=from_data)

        if serializer_instance.valid():

            serializer_instance.save(owner=auth_user)#form_data * owner

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)



   
   
   
   
from transactions.permissions import isOwner   
   
class ExpenseRetrieveUpdateDeleteView(APIView): 

    authentication_classes=[authentication.BaseAuthentication]

   # permission_classes=[permissions.IsAuthenticated] 
    
    permission_classes=[isOwner]

    def get(self,request,pk=None):
        
        qs=get_object_or_404(Expense,id=pk)

        self.check_object_permissions(request,qs)
        
        serializer_instance=ExpenseSerializer(qs)

        return Response(serializer_instance.data)


    def put(self,request,pk=None):

        instance=get_object_or_404(Expense,pk=None)

        self.check_object_permissions(request,instance)

        form_data=request.data

        serializer_instance=ExpenseSerializer(data=form_data,instance=instance)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(serializer_instance.data)
        
        else:

            return Response(serializer_instance.errors)

           

    
    
    

    


    def delete(self,request,pk=None):

        instance=get_object_or_404(Expense,id=pk)

        self.check_object_permissions(request,instance)

        instance.delete()

        return Response({"message":"deleted"})



from datetime import datetime
from django.db.models import Sum



class ExpenseSummeryView(APIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):

        auth_user_expenses=Expense.objects.filter(owner=request.user)

        response_data={
            "todays_total":0,
            "monthly_total":0
        }



        cur_date=datetime.today().date()

        todays_total= auth_user_expenses.filter(created_at_date=cur_date).values("amount").aggregate(total=Sum("amount")).get("total")

        #todays_total=3200

        #current_month total

        cur_month=datetime.today().month

        cur_year=datetime.today().year

        monthly_total_amount=auth_user_expenses.filter(created_at__month=cur_month,
                                                       created_at__year=cur_year).values("amount").aggregate(total=Sum("amount")).get("total")

        response_data["monthly_total_amount"]=monthly_total_amount

        response_data["todays-total"]=todays_total

        return Response(response_data)






    

        
        




        





from rest_framework import serializers

from transactions.models import User



class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:

        model=User

        fields="__all__"

        read_only=["id","owner","created_at"]


    



from django.forms import ValidationError
from rest_framework.serializers import ModelSerializer
from base.models import CallLog

class CallLogSerializer(ModelSerializer):
    class Meta:
        model = CallLog
        fields = '__all__'
    def validate_from_number(self,value):
        if len(value)<10 or len(value)>10:
            raise ValidationError("Number should not be less than or greater than 10 characters")
        
    def validate_to_number(self,value):
        if len(value)<10 or len(value)>10:
            raise ValidationError("Number should not be less than or greater than 10 characters")
        
    def update(self,instance,validated_data):
        instance.from_number = validated_data.get('from_number',instance.from_number)
        instance.to_number = validated_data.get('from_number',instance.to_number)
        instance.save()
        return instance


    

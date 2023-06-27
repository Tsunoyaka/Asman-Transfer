from rest_framework import serializers

from .utils import normalize_phone
from .tasks import send_report_form

from .models import Transfer


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ('name', 'phone', 'date', 'time', 
                  'route', 'auto', 'place_departure')
        
    def validate_phone(self, phone):
        phone = normalize_phone(phone)
        if len(phone) != 13:
            raise serializers.ValidationError('Неверный формат телефона')
        return phone
    
    def create(self, validated_data):
        name = validated_data.get('name')
        phone = validated_data.get('phone')
        date = validated_data.get('date')
        time = validated_data.get('time')
        route = validated_data.get('route')
        auto = validated_data.get('auto')
        place_departure = validated_data.get('place_departure')
        send_report_form.delay(name=name, phone=phone, route=route, date=date, 
                         time=time, auto=auto.title, place_departure=place_departure, price=auto.price, contract_price=auto.contract_price)
        return super().create(validated_data)
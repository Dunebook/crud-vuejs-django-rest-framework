from rest_framework import serializers
from .models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('id', 'name', 'description', 'currency',
            'amount', 'created_at', 'updated_at'
        )
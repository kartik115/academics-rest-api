from rest_framework import serializers


class TimeStampedModelSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(
        format="%m/%d/%Y %H:%M:%S",
        input_formats="%m/%d/%Y %H:%M:%S",
        read_only=True
    )
    last_updated_at = serializers.DateTimeField(
        format="%m/%d/%Y %H:%M:%S",
        input_formats="%m/%d/%Y %H:%M:%S",
        read_only=True
    )

    class Meta:
        fields = ('created_at', 'last_updated_at',)

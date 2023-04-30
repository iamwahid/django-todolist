from rest_framework import serializers

from .models import Activity

# create Activity serializer
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'title', 'email', 'created_at', 'updated_at']
        # extra kwargs
        extra_kwargs = {
            "id": {
                "read_only": True
            },
            "created_at": {
                "read_only": True
            },
            "updated_at": {
                "read_only": True
            }
        }

    def to_internal_value(self, data):
        if "title" not in data:
            raise serializers.ValidationError({"title": "title cannot be null"})
        if "title" in data and len(data["title"]) == 0:
            raise serializers.ValidationError({"title": "title cannot be null"})
        internal_value = super().to_internal_value(data)
        return internal_value

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["createdAt"] = representation.pop("created_at")
        representation["updatedAt"] = representation.pop("updated_at")
        return representation
from rest_framework import serializers

from .models import Todo

# create Todo serializer
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'activity_group', 'title', 'priority', 'is_active', 'created_at', 'updated_at']
        extra_kwargs = {
            "id": {
                "read_only": True
            },
            "created_at": {
                "read_only": True
            },
            "updated_at": {
                "read_only": True
            },
            "title": {
                "required": False
            },
        }

    def to_internal_value(self, data):
        if not self.instance:
            if "title" not in data:
                raise serializers.ValidationError({"title": "title cannot be null"})
            if "title" in data and len(data["title"]) == 0:
                raise serializers.ValidationError({"title": "title cannot be null"})
            if "activity_group_id" not in data:
                raise serializers.ValidationError({"activity_group_id": "activity_group_id cannot be null"})
            if "activity_group_id" in data and data["activity_group_id"] == None:
                raise serializers.ValidationError({"activity_group_id": "activity_group_id cannot be null"})
        if "activity_group_id" in data:
            data["activity_group"] = data.pop("activity_group_id")
        internal_value = super().to_internal_value(data)
        return internal_value

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["activity_group_id"] = representation.pop("activity_group")
        representation["createdAt"] = representation.pop("created_at")
        representation["updatedAt"] = representation.pop("updated_at")
        return representation

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.priority = validated_data.get("priority", instance.priority)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.save()
        return instance
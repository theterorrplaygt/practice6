from rest_framework import serializers
from .models import Category, Task, Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class TaskSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'status',
                  'category', 'category_id', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    task = serializers.StringRelatedField(read_only=True)
    task_id = serializers.PrimaryKeyRelatedField(
        queryset=Task.objects.all(), source='task', write_only=True
    )
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'task', 'task_id', 'text', 'user', 'created_at']
        read_only_fields = ['user']
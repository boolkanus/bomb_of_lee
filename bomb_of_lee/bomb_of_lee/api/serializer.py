from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User


# 정윤재 : 안녕하세요. rest api만드려면 , 시리얼라이저를 만들어야 한다고 해서 일단 파일을 올립니다.
# 모델링 데이터에 맞춰서 진행해야합니다.

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email')

# class PostSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True)
#     class Meta:
#         model = Post
#         fields = (
#             'id',
#             'title',
#             'subtitle',
#             'content',
#             'created_at',
#         )
#         read_only_fields = ('created_at',)
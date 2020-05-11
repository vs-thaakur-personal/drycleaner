import uuid

from rest_framework import serializers
from auth.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'middle_name', 'last_name', 'email', 'user_id', 'address',
                  'phone_no', 'alt_phone_no', 'password', 'email', 'area', 'id')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        user = User.objects.create(
            # id=self.validated_data['id'],
            phone_no=self.validated_data['phone_no'],
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            user_id=f'{self.validated_data["first_name"]}_{uuid.uuid1()}',
            middle_name=self.validated_data['middle_name'],
            address=self.validated_data['address'],
            alt_phone_no=self.validated_data['alt_phone_no'],
            area=self.validated_data['area'],
        )
        user.set_password(self.validated_data['password'])
        user.save()
        return user

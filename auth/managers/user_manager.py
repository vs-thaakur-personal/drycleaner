import uuid

from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, first_name, address, phone_no, password):
        if not first_name:
            raise ValueError("Please Provide First Name")
        if not address:
            raise ValueError("Please Provide Address")
        if not phone_no:
            raise ValueError("Please Provide phone_no")
        if not password:
            raise ValueError("Please Provide password")

        user = self.model(first_name=first_name,
                          address=address,
                          phone_no=phone_no)
        user.user_id = f'{first_name}_{uuid.uuid1()}'
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, first_name, address, phone_no, password):
        user = self.model(first_name=first_name,
                          address=address,
                          phone_no=str(phone_no),
                          password=password)
        user.user_id = f'{first_name}_{uuid.uuid1()}'
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user

from django.contrib.auth.models import BaseUserManager
from django.core.validators import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("Please enter a valid email"))
    
    def create_user(self, email, first_name,last_name, password, **extra_fields):
        if email:
            email=self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("am email required"))
        if not first_name:
            raise ValueError(_("first name required"))
        if not last_name:
            raise ValueError(_("last name required"))

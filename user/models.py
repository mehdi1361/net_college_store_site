from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group
from django.contrib.auth.models import BaseUserManager


Group.add_to_class(
    'description',
    models.TextField(
        null=True,
        blank=True
    )
)

class Roles(Group):
    class Meta:
        proxy = True
        verbose_name = verbose_name_plural = 'Roles'
        
class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email or len(email) <= 0:
            raise ValueError("Email field is required !")
        if not password:
            raise ValueError("Password is must !")

        user = self.model(
            email=self.normalize_email(email),
        )
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    father_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=200, unique=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    is_teacher = models.BooleanField(default=False)

    image = models.ImageField(
        verbose_name=_("image"),
        upload_to="users",
        null=True,
        blank=True
    )

    description = models.TextField(
        verbose_name=_("description"),
        help_text=_("description for any user"),
        null=True
    )

    cv_file = models.FileField(verbose_name=_("cv file"), upload_to="user/cv", null=True, blank=True)
    ns_image = models.ImageField(verbose_name=_("national card image"),upload_to="user/national_card", null=True, blank=True)

    USERNAME_FIELD = "email"
    objects = UserAccountManager()

    def __str__(self):
        return str(self.email)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):

        return super().save(*args, **kwargs)

    def img_preview(self):
        try:
            return mark_safe(f'<img src="{self.image.url}" width = "50" height="40" alt="">')
        except Exception as e:
            return ""

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
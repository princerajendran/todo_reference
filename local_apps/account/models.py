import uuid
import shortuuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from local_apps.account.managers import CustomUserManager

ROLE = (
    ("Admin", "Admin"),
    ('User', "User"),
    ("Other", "Other"),
)


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    date_joined = None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    account_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })
    mobile = models.CharField(max_length=13, unique=True, blank=True, null=True,
                              error_messages={
                                  'unique': "A user with that mobile already exists.",
                              })
    image = models.ImageField(blank=True, null=True, upload_to='account/user/image')
    role = models.CharField(choices=ROLE, max_length=15, default='User',
                            help_text='Id generation depends on the role. Once you submit it will be permanent.')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ["-created_at"]
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if not self.account_id:
            self.account_id = 'ACC-ID-' + shortuuid.ShortUUID().random(length=12)

        super().save(*args, **kwargs)

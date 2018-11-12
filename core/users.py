from django.contrib.auth.models import User
from django.db import models
from django.contrib.postgres.fields import JSONField
from .models import TimeAuditModel


class Profile(TimeAuditModel):
    """Model definition for Profile."""

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name="profile")

    # AGE, Streak
    # XP per Day, Time per Day
    # 5, 10, 15, 20mins
    # 5, 10, 20, 50
    # Organisation.
    details = JSONField(null=True)

    # settings = JSONField(null=True)

    def has_details(self):
        if self.details:
            return True
        else:
            return False

    class Meta:
        """Meta definition for Profile."""

        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.user.username


class SocialProvider(TimeAuditModel):
    """
    Model definition for SocialProvider.
    """
    SOCIAL_PROVIDERS = (
        ('FACEBOOK', 'Facebook'),
        ('GOOGLE', 'Google'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    provider = models.CharField(max_length=255,
                                choices=SOCIAL_PROVIDERS)
    extra = JSONField(null=True)

    class Meta:
        """Meta definition for SocialProvider."""

        verbose_name = 'SocialProvider'
        verbose_name_plural = 'SocialProviders'

    def __str__(self):
        """Unicode representation of SocialProvider."""
        pass

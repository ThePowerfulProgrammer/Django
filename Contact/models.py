from django.db import models
from django.core.validators import EmailValidator

class Contact(models.Model):
    """A model for storing contact requests from users."""
    
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=True, validators=[EmailValidator])
    subject = models.CharField(max_length=40, blank=False)
    body = models.TextField(max_length=500, blank=False)

    def __str__(self) -> str:
        """Return a human-readable representation of the object."""
        return f"{self.name}: {self.subject}"
    
    def __repr__(self) -> str:
        return f"{self.name}: {self.subject}"

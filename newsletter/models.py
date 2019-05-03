from django.db import models

class NewSletters(models.Model):

    email = models.EmailField()

    class Meta:

        verbose_name = "Newsletter"

        verbose_name_plural = "Newsletters"

    def __str__(self):

        return self.email

from django.db import models

class RoommateProfile(models.Model):
    SLEEP_CHOICES = [('early','Early sleeper'),('normal','Normal'),('late','Late sleeper')]
    CLEAN_CHOICES = [('low','Relaxed'),('medium','Moderate'),('high','Very clean')]
    FOOD_CHOICES = [('veg','Vegetarian'),('nonveg','Non-vegetarian'),('both','Both are okay')]
    SMOKE_CHOICES = [('never','Never'),('sometimes','Sometimes'),('yes','Regularly')]
    SOCIAL_CHOICES = [('quiet','Quiet/private'),('balanced','Balanced'),('social','Very social')]
    NOISE_CHOICES = [('quiet','Needs quiet'),('moderate','Moderate noise'),('loud','Okay with noise')]
    GUEST_CHOICES = [('rare','Rare guests'),('sometimes','Sometimes'),('often','Frequent guests')]

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=20)
    city = models.CharField(max_length=80, default='Vadodara')
    budget = models.PositiveIntegerField(help_text='Monthly budget in INR')
    sleep = models.CharField(max_length=20, choices=SLEEP_CHOICES)
    cleanliness = models.CharField(max_length=20, choices=CLEAN_CHOICES)
    food = models.CharField(max_length=20, choices=FOOD_CHOICES)
    smoking = models.CharField(max_length=20, choices=SMOKE_CHOICES)
    social = models.CharField(max_length=20, choices=SOCIAL_CHOICES)
    noise = models.CharField(max_length=20, choices=NOISE_CHOICES)
    guests = models.CharField(max_length=20, choices=GUEST_CHOICES)
    cooking = models.BooleanField(default=True)
    study_work = models.BooleanField(default=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

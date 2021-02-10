from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()  # assign a user

# the first value is the one that gets stored in the db, display value is the second one
SOURCE_CHOICES = (
    ('YouTube', 'YouTube'),
    ('Google', 'Google'),
    ('Newsletter', 'Newsletter'),
    ('LinkedIn', 'LinkedIn'),
    ('Web Scrape', 'Web Scrape'),
    ('Poach', 'Poach')
)


class Agent(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return first_name + last_name


class Lead(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    age = models.IntegerField(default=0)
    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCE_CHOICES, max_length=50) # where lead was sourced

    profile_pic = models.ImageField(blank=True, null=True)
    special_files = models.FileField(blank=True, null=True)  # not all leads have files associated

    # creating relationships between tables
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)  # if defined before Agent, put it in quotation marks

    #agent = models.ForeignKey("Agent", on_delete=models.SET_NULL, null=true)
    #agent = models.ForeignKey("Agent", on_delete=models.SET_DEFAULT, default=true)





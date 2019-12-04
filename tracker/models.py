from django.db import models

from django.utils.translation import gettext as _

class Squirrel(models.Model):
    latitude = models.FloatField(
        help_text=_('Latitude of squirrel sighting point'),
    )

    longitude = models.FloatField(
        help_text=_('Longitude of squirrel sighting point'),
    )

    unique_squirrel_ID = models.CharField(
        help_text=_('ID for each squirrel sighting'),
        max_length=20,
        unique=True,
        primary_key=True,
    )

    AM = 'AM'
    PM = 'PM'
    SHIFT_CHOICES = (
        (AM, 'AM'),
        (PM, 'PM'),
    )

    shift = models.CharField(
        help_text=_('Shift of the day'),
        max_length=5,
        choices=SHIFT_CHOICES,
        default=AM,
    )

    date = models.DateField(
        help_text=_('Date of sighting'),
    )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    UNKNOWN = ''

    AGE_CHOICES = (
        (ADULT, 'Adult'),
        (JUVENILE, 'Juvenile'),
        (UNKNOWN, ''),
    )

    age = models.CharField(
        help_text=_('Age of the squirrel'),
        max_length=10,
        choices=AGE_CHOICES,
        default=UNKNOWN,
    )

    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'
    UNKNOWN = ''
    
    COLOR_CHOICES = (
        (GRAY, 'Gray'),
        (CINNAMON, 'Cinnamon'),
        (BLACK, 'Black'),
        (UNKNOWN, ''),
    )

    primary_fur_color = models.CharField(
        help_text=_('Primary fur color of the squirrel'),
        max_length=10,
        choices=COLOR_CHOICES,
        default=UNKNOWN,
    )

    GP = 'Ground Plane'
    AG = 'Above Ground'
    UNKNOWN = ''

    LOCATION_CHOICES = (
        (GP, 'Ground Plane'),
        (AG, 'Above Ground'),
        (UNKNOWN, ''),
    )

    location = models.CharField(
        help_text=_('Location of the squirrel'),
        max_length=20,
        choices=LOCATION_CHOICES,
        default=UNKNOWN,
    )

    specific_location = models.CharField(
        help_text=_('Specific location of the squirrel'),
        max_length=200,
    )

    running = models.BooleanField(
        help_text=_('Whether the squirrel was seen running'),
        default=False,
    )

    chasing = models.BooleanField(
        help_text=_('Whether the squirrel was seen chasing another squirrel'),
        default=False,
    )

    climbing = models.BooleanField(
        help_text=_('Whether the squirrel was seen climbing'),
        default=False,
    )

    eating = models.BooleanField(
        help_text=_('Whether the squirrel was seen eating'),
        default=False,
    )

    foraging = models.BooleanField(
        help_text=_('Whether the squirrel was seen foraging for food'),
        default=False,
    )

    other_activities = models.CharField(
        help_text=_('Other activities of the squirrel'),
        max_length=200,
    )

    kuks = models.BooleanField(
        help_text=_('Whether the squirrel was heard kukking'),
        default=False,
    )

    quaas = models.BooleanField(
        help_text=_('Whether the squirrel was heard quaaing'),
        default=False,
    )

    moans = models.BooleanField(
        help_text=_('Whether the squirrel was heard moaning'),
        default=False,
    )

    tail_flags = models.BooleanField(
        help_text=_('Whether the squirrel was seen flagging tail'),
        default=False,
    )

    tail_twitches = models.BooleanField(
        help_text=_('Whether the squirrel was seen twitching tail'),
        default=False,
    )

    approaches = models.BooleanField(
        help_text=_('Whether the squirrel was seen approaching human'),
        default=False,
    )

    indifferent = models.BooleanField(
        help_text=_('Whether the squirrel was indifferent to human'),
        default=False,
    )

    runs_from = models.BooleanField(
        help_text=_('Whether the squirrel was seen running from human'),
        default=False,
    )

    def __str__(self):
        return self.unique_squirrel_ID
# Create your models here.

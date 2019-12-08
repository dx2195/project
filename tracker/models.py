from django.db import models

from django.utils.translation import gettext as _

class Squirrel(models.Model):
    latitude = models.FloatField(
        help_text = _('Latitude of squirrel sighting point'),
    )

    longitude = models.FloatField(
        help_text = _('Longitude of squirrel sighting point'),
    )

    unique_squirrel_ID = models.CharField(
        help_text = _('ID for each squirrel sighting'),
        max_length = 20,
        unique = True,
        primary_key = True,
    )

    AM = 'AM'
    PM = 'PM'
    SHIFT_CHOICES = (
        (AM, 'AM'),
        (PM, 'PM'),
    )

    shift = models.CharField(
        help_text = _('Shift of the day'),
        max_length = 5,
        choices = SHIFT_CHOICES,
        default = AM,
    )

    date = models.DateField(
        help_text = _('Date of sighting'),
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
        help_text = _('Age of the squirrel'),
        max_length = 10,
        choices = AGE_CHOICES,
        default = UNKNOWN,
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
        help_text = _('Primary fur color of the squirrel'),
        max_length = 10,
        choices = COLOR_CHOICES,
        default = UNKNOWN,
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
        help_text = _('Location of the squirrel'),
        max_length = 20,
        choices = LOCATION_CHOICES,
        default = UNKNOWN,
    )

    specific_location = models.CharField(
        help_text = _('Specific location of the squirrel'),
        max_length = 200,
        blank = True,
    )

    T = 'TRUE'
    F = 'FALSE'

    TF_CHOICES = (
        (T, 'TRUE'),
        (F, 'FALSE'),
    )

    running = models.CharField(
        help_text = _('Whether the squirrel was seen running'),
        max_length = 10,
        choices = TF_CHOICES,
        default = F,
    )

    chasing = models.CharField(
        help_text = _('Whether the squirrel was seen chasing another squirrel'),
        max_length = 10,
        choices = TF_CHOICES,
        default = F,
    )

    climbing = models.CharField(
        help_text = _('Whether the squirrel was seen climbing'),
        max_length = 10,
        choices = TF_CHOICES,
        default = F,
    )

    eating = models.CharField(
        help_text = _('Whether the squirrel was seen eating'),
        max_length = 10,
        choices = TF_CHOICES,
        default = F,
    )

    foraging = models.CharField(
        help_text = _('Whether the squirrel was seen foraging for food'),
        max_length = 10,
        choices = TF_CHOICES,
        default = F,
    )

    other_activities = models.CharField(
        help_text = _('Other activities of the squirrel'),
        max_length = 200,
        blank = True,
    )

    kuks = models.CharField(
        help_text = _('Whether the squirrel was heard kukking'),
        max_length = 10,
        choices = TF_CHOICES,
        default = F,
    )

    quaas = models.CharField(
        help_text = _('Whether the squirrel was heard quaaing'),
        max_length = 10,
        choices = TF_CHOICES,
        default = F,
    )

    moans = models.CharField(
        help_text = _('Whether the squirrel was heard moaning'),
        max_length = 10,
        choices = TF_CHOICES,
        default = F,
    )

    tail_flags = models.CharField(
        help_text = _('Whether the squirrel was seen flagging tail'),
        max_length = 10,
        choices = TF_CHOICES,
        default = F,
    )

    tail_twitches = models.CharField(
        help_text = _('Whether the squirrel was seen twitching tail'),
        max_length = 10,
        choices = TF_CHOICES,
        default = F,
    )

    approaches = models.CharField(
        help_text = _('Whether the squirrel was seen approaching human'),
        max_length = 10,
        choices = TF_CHOICES,
        default = F,
    )

    indifferent = models.CharField(
        help_text = _('Whether the squirrel was indifferent to human'),
        max_length = 10,
        choices = TF_CHOICES,
        default = F,
    )

    runs_from = models.CharField(
        help_text = _('Whether the squirrel was seen running from human'),
        max_length = 10,
        choices = TF_CHOICES,
        default = F,
    )

    def __str__(self):
        return self.unique_squirrel_ID
# Create your models here.

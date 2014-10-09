from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user_id         = models.OneToOneField(User)
    institution     = models.CharField(max_length=100, null=True, blank=True)
    phone_number    = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "%s's profile" % self.user

def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)

class Domain(models.Model):
    name        = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Kingdom(models.Model):
    name        = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    domain_id   = models.ForeignKey(Domain)

    def __str__(self):
        return self.name

class Phylum(models.Model):
    name        = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    kingdom_id  = models.ForeignKey(Kingdom)

    def __str__(self):
        return self.name

class Class(models.Model):
    name        = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    phylum_id   = models.ForeignKey(Phylum)

    def __str__(self):
        return self.name

class Order(models.Model):
    name        = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    class_id    = models.ForeignKey(Class)

    def __str__(self):
        return self.name

class Family(models.Model):
    name        = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    order_id    = models.ForeignKey(Order)

    def __str__(self):
        return self.name

class Genus(models.Model):
    name        = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    family_id      = models.ForeignKey(Family)

    def __str__(self):
        return self.name

class ConservationStatus(models.Model):
    code    = models.CharField(max_length=2)
    name    = models.CharField(max_length=255)
    order   = models.IntegerField()

    def __str__(self):
        return self.name

class Species(models.Model):
    name                    = models.CharField(max_length=255)
    common_name             = models.CharField(max_length=255, null=True, blank=True)
    genus_id                = models.ForeignKey(Genus)
    conservation_status_id  = models.ForeignKey(ConservationStatus)
    gestation_period        = models.IntegerField(null=True, blank=True) # or incubation
    clutch_interval         = models.IntegerField(null=True, blank=True)
    medium_lifespan         = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Studbook (models.Model):
    name                = models.CharField(max_length=255)
    species_id          = models.ForeignKey(Species)
    user_id             = models.ForeignKey(User)
    currentness         = models.DateField('currentness')
    creation_date       = models.DateTimeField('creation date')
    modification_date   = models.DateTimeField('modification date')
    scope               = models.CharField(max_length=100, null=True, blank=True) # International, European, etc

    def __str__(self):
        return self.name

class Specimen (models.Model):
    studbook_id                     = models.ForeignKey(Studbook)
    species_id                      = models.ForeignKey(Species)
    gan                             = models.CharField(max_length=100, null=True, blank=True) # ZIMS GAN
    local_id                        = models.CharField(max_length=100, null=True, blank=True)
    house_name                      = models.CharField(max_length=100, null=True, blank=True)
    sex                             = models.CharField(max_length=100, null=True, blank=True) # not only male/female
    hybrid_status                   = models.CharField(max_length=100, null=True, blank=True)
    enclosure                       = models.CharField(max_length=100, null=True, blank=True)
    rearing                         = models.CharField(max_length=100, null=True, blank=True)
    dam_id                          = models.ForeignKey('self', related_name='Specimen_Dam', null=True, blank=True)
    sire_id                         = models.ForeignKey('self', related_name='Specimen_Sire', null=True, blank=True)
    birth_type                      = models.CharField(max_length=100, null=True, blank=True)
    birth_location                  = models.CharField(max_length=100, null=True, blank=True)
    birth_date                      = models.DateField('birth date', null=True, blank=True)
    tag                             = models.CharField(max_length=100, null=True, blank=True) # tag/brand
    transponder                     = models.CharField(max_length=100, null=True, blank=True) # transponder ID
    transponder_location            = models.CharField(max_length=100, null=True, blank=True)
    regional_associations           = models.CharField(max_length=100, null=True, blank=True) # related to the next 2 fields
    # ARAZPA (Australia/NZ), AZA (North America), CAZG (China), CAZA (Canada), CZAI (India), EAZA(Europe),
    # BIAZA (Britain), IZPA (Indonesia), JAZA (Japan), PAAZAB (Africa), SEAZA (SE Asia), SZB (Brasil), Other, International
    regional_studbook_number        = models.CharField(max_length=100, null=True, blank=True)
    international_studbook_number   = models.CharField(max_length=100, null=True, blank=True)
    old_accession_number            = models.CharField(max_length=100, null=True, blank=True)
    old_accession_institution       = models.CharField(max_length=100, null=True, blank=True)
    tatoo_number                    = models.CharField(max_length=100, null=True, blank=True) # or FB
    tatoo_location                  = models.CharField(max_length=100, null=True, blank=True)
    breeder_number                  = models.CharField(max_length=100, null=True, blank=True)
    permits_id                      = models.CharField(max_length=100, null=True, blank=True) # name (CITES, Marine Mammal Permit, Endangered Species, Post Entry Quarantine, etc), number
    color_phase                     = models.CharField(max_length=100, null=True, blank=True)
    weight                          = models.CharField(max_length=100, null=True, blank=True)
    length                          = models.CharField(max_length=100, null=True, blank=True)
    clutch                          = models.CharField(max_length=100, null=True, blank=True)
    notching_mark                   = models.CharField(max_length=100, null=True, blank=True)
    notch_location                  = models.CharField(max_length=100, null=True, blank=True)
    vendors_taxon                   = models.CharField(max_length=100, null=True, blank=True)
    sire_taxon                      = models.CharField(max_length=100, null=True, blank=True)
    dam_taxon                       = models.CharField(max_length=100, null=True, blank=True)
    old_studbook_number             = models.CharField(max_length=100, null=True, blank=True)
    death_number                    = models.CharField(max_length=100, null=True, blank=True)
    growth_stage                    = models.CharField(max_length=100, null=True, blank=True) # (Infant, Juvenile, Adult / HAtchling, Chick / Tadpole, etc)
    carcass_recipient               = models.CharField(max_length=100, null=True, blank=True)
    parent_assumptions              = models.TextField(null=True, blank=True)
    egg_lay_date                    = models.CharField(max_length=100, null=True, blank=True) # only for birds
    fledge_date                     = models.CharField(max_length=100, null=True, blank=True) # only for birds
    general_notes                   = models.TextField(null=True, blank=True)
    behavior_notes                  = models.TextField(null=True, blank=True)
    physical_condition              = models.TextField(null=True, blank=True)
    medical_notes                   = models.TextField(null=True, blank=True)
    reproductive_notes              = models.TextField(null=True, blank=True)

    def __str__(self):
        if self.house_name:
            return str(self.gan) + ' - ' + self.house_name
        else:
            return str(self.gan)

class EventType (models.Model):
    name                    = models.CharField(max_length=100)
    location_field          = models.BooleanField()
    local_id_field          = models.BooleanField()
    management_plan_field   = models.BooleanField()
    egg_transfer_field      = models.BooleanField()
    institution_field       = models.BooleanField()
    social_group_field      = models.BooleanField()
    # Management Plan In -> Regional Cooperative Management Plan
    # Management Plan Surplus -> Regional Cooperative Management Plan
    # Management Plan Out -> Regional Cooperative Management Plan
    # Birth/Hatch -> Location, Local ID, Egg transfer?
    # Sale -> Location, Local ID,
    # Purchase -> Location, Local ID,
    # Donation -> Location, Local ID,
    # Wild Caught -> Location, Local ID
    # Transfer -> Location, Local ID
    # Death -> Location
    # Release -> Location, Local ID
    # Social In -> Institution, Social Group
    # Social Out -> Institution, Social Group
    # Pending Transfer -> Location, Local ID

    def __str__(self):
        return self.name

class Event (models.Model):
    specimen_id         = models.ForeignKey(Specimen)
    event_type_id       = models.ForeignKey(EventType)
    date                = models.DateField('event date')                                # For all types: Transaction date or other date
    date_estimate       = models.CharField(max_length=2, null=True, blank=True)         # For all types: date estimate: D (in days), M (in months), M# (range month), Y (in years), R# (range in years), U (Unknown)
    location            = models.CharField(max_length=100, null=True, blank=True)
    local_id            = models.CharField(max_length=100, null=True, blank=True)
    social_group        = models.CharField(max_length=100, null=True, blank=True)
    egg_transfer        = models.NullBooleanField()
    management_plan     = models.CharField(max_length=100, null=True, blank=True)       # Regional Cooperative Management Plan
    institution         = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.specimen_id) + ' - ' + str(self.event_type_id)

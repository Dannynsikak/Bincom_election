from django.db import models

class AgentName(models.Model):
    name_id = models.IntegerField(primary_key=True, null=False)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255, null=True, default=None)
    phone = models.CharField(max_length=13)
    PollingUnit_uniqueid = models.IntegerField()
    
    class Meta:
        db_table = 'agentname'

class AnnouncedLGAResults(models.Model):
    result_id = models.IntegerField(primary_key=True)
    lga_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(null=True, blank=True)
    user_ip_address = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'announced_lga_results'

class AnnouncedPUResults(models.Model):
    result_id = models.IntegerField(primary_key=True)
    polling_unit_uniqueid = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50, null=False)
    date_entered = models.DateTimeField(null=True, blank=True,auto_now_add=True)
    user_ip_address = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'announced_pu_results'

class AnnouncedStateResults(models.Model):
    result_id = models.IntegerField(primary_key=True)
    state_name = models.CharField(max_length=50)
    party_abreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50, null=False)
    date_entered = models.DateTimeField(null=True, blank=True)
    user_ip_address = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'announced_state_results'

class AnnouncedWardResults(models.Model):
    result_id = models.IntegerField(primary_key=True)
    ward_name = models.CharField(max_length=50)
    party_abreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50, null=False)
    date_entered = models.DateTimeField(null=True, blank=True)
    user_ip_address = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'announced_ward_results'

class LGA(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    lga_id = models.IntegerField()
    lga_name = models.CharField(max_length=50)
    state_id = models.IntegerField()
    lga_description = models.TextField(null=True, blank=True)
    entered_by_user = models.CharField(max_length=50, null=False)
    date_entered = models.DateTimeField(null=True, blank=True)
    user_ip_address = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'lga'

class Party(models.Model):
    id = models.IntegerField(primary_key=True)
    partyid = models.CharField(max_length=11)
    partyname = models.CharField(max_length=11)
    
    class Meta:
        db_table = 'party'

class PollingUnit(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    polling_unit_id = models.IntegerField()
    ward_id = models.IntegerField()
    lga_id = models.IntegerField()
    uniquewardid = models.IntegerField(null=True, default=None)
    polling_unit_number = models.CharField(max_length=50, null=True, default=None)
    polling_unit_name = models.CharField(max_length=50, null=True, default=None)
    polling_unit_description = models.TextField(null=True, blank=True)
    lat = models.CharField(max_length=255, null=True, default=None)
    long = models.CharField(max_length=255, null=True, default=None)
    entered_by_user = models.CharField(max_length=50, null=True, default=None)
    date_entered = models.DateTimeField(null=True, blank=True)
    user_ip_address = models.CharField(max_length=50, null=True, default=None)
    
    class Meta:
        db_table = 'polling_unit'

class States(models.Model):
    state_id = models.IntegerField(primary_key=True)
    state_name = models.CharField(max_length=50, null=False)
    
    class Meta:
        db_table = 'states'

class Ward(models.Model):
    uniqueid = models.IntegerField()
    ward_id = models.IntegerField()
    ward_name = models.CharField(max_length=50)
    lga_id = models.IntegerField()
    ward_description = models.TextField(null=True, blank=True)
    entered_by_user = models.CharField(max_length=50, null=False)
    date_entered = models.DateTimeField(null=True, blank=True)
    user_ip_address = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'ward'

from django.db import models

'''
Models the user to user interactions 
'''

# Many to one 
# self = car class (many)
# self.FK(Manufacturer) manufacturer is one 

class UserUser(models.Model):
	uuid = models.IntegerField(db_index=True, unique=True)
	uid1 = models.ForeignKey("helpdesk.UserProfile")
	uid2 = models.ForeignKey("helpdesk.UserProfile")

	def _first(self):
		return min(map(lambda interaction: interaction.created, self.interaction_set.all()))


class Interaction(models.Model):
	interaction_id = models.IntegerField(db_index=True, unique=True)
	uuid = models.ForeignKey("helpdesk.UserUser")

	created = models.DateTimeField(auto_now_add=True)

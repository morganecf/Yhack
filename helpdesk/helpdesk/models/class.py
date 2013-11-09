from django.db import models

class Class(models.Model):
	cid = models.IntegerField(db_index=True)
	title = models.CharField()
	


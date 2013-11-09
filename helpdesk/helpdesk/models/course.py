from django.db import models

class Course(models.Model):
	course_id = models.IntegerField(db_index=True, unique=True)
	code = models.CharField(max_length=8, unique=True)
	short_name = models.CharField(max_length=55)
	#description = models.TextField(blank=True, null=True)





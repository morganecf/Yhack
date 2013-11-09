from django.db import models

class UserCourse(models.Model):
	user_course_id = models.IntegerField(db_index=True, unique=True)
	user = models.ForeignKey("helpdesk.UserProfile")
	course = models.ForeignKey("helpdesk.Course")
	current = models.BooleanField()

	joined = models.DateTimeField(auto_now_add=True)


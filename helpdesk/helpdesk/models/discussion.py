from django.db import models

'''
Each discussion is associated with a class. 
'''

class Discussion(models.Model):
	discussion_id = models.IntegerField(db_index=True, unique=True)
	poster = models.ForeignKey("helpdesk.UserProfile", unique=True)
	course = models.ForeignKey("helpdesk.Course")
	title = models.CharField(max_length=255)
	text = models.TextField()

	created = models.DateTimeField(auto_now_add=True)

	def _num_comments(self):
		return len(self.comment_set.all())

class Comment(models.Model):
	comment_id = models.IntegerField(db_index=True, unique=True)
	poster = models.ForeignKey("helpdesk.UserProfile", unique=True)
	discussion = models.ForeignKey(Discussion)
	text = models.TextField()

	created = models.DateTimeField(auto_now_add=True)

from django.db import models

'''
One Docuum object is associated with one course. 
'''

class Docuum(models.Model):
	docuum_id = models.IntegerField(db_index=True, unique=True)
	course = models.ForeignKey("helpdesk.Course")

	def _total(self):
		return len(self.docuument_set.all())

class Docuument(models.Model):
	doc_id = models.IntegerField(db_index=True, unique=True)
	docuum = models.ForeignKey(Docuum)
	title = models.CharField(max_length=100)
	url = models.CharField(max_length=200)

	SYLLABUS = 'S'
	NOTES = 'N'
	ASSIGNMENT = 'A'
	MIDTERM = 'M'
	EXAM = 'E'
	SOLUTION = 'S'

	DOC_TYPES = (
			(EXAM, "exam"),
			(SYLLABUS, "syllabus"),
			(MIDTERM, "midterm"),
			(ASSIGNMENT, "assignment"),
			(SOLUTION, "solution"),
			(NOTES, "notes"),
		)

	doc_type = models.CharField(max_length=2, choices=DOC_TYPES)


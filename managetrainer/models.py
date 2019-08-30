from django.db import models
from django.core.urlresolvers import reverse


class Trainer(models.Model):
    emp_id = models.CharField(primary_key=True, max_length=45)
    emp_name = models.CharField(max_length=45)
    gender = models.CharField(max_length=45)
    salary = models.FloatField()
    doj = models.DateField()
    profile_pic = models.FileField(default=None)

    def get_absolute_url(self):
        return reverse('managetrainer:home')

    def __str__(self):
        return 'emp_id = {}'.format(self.emp_id)


class Batches(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    batch_code = models.CharField(max_length=10)
    batch_name = models.CharField(max_length=45)
    status = models.BooleanField(default=False)

    def __str__(self):
        return 'Batch Code = {}'.format(self.batch_code)

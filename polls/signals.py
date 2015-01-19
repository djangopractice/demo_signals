from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from polls.models import Question, Choice
import os.path


@receiver(pre_delete, sender=Question)
@receiver(pre_delete, sender=Choice)
@receiver(pre_save, sender=Question)
@receiver(pre_save, sender=Choice)
def model_pre_change(sender, **kwargs):
    if os.path.isfile(settings.READ_ONLY_FILE):
        raise ReadOnlyException('Model in read only mode, cannot save')


@receiver(post_save, sender=Question)
@receiver(post_save, sender=Choice)
def model_post_save(sender, **kwargs):
    if kwargs['created'] is True:
        print('Created: {}'.format(kwargs['instance'].__dict__))
    else:
        print('Updated: {}'.format(kwargs['instance'].__dict__))


@receiver(post_delete, sender=Question)
@receiver(post_delete, sender=Choice)
def model_post_delete(sender, **kwargs):
    print('Deleted: {}'.format(kwargs['instance'].__dict__))


class ReadOnlyException(Exception):
    pass

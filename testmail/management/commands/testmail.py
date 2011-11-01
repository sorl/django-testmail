import datetime
from django.core.management.base import BaseCommand, CommandError
from django.core.mail import EmailMessage


class Command(BaseCommand):
    help = 'Sends a test mail.'

    def handle(self, *args, **options):
        if len(args) == 0:
            email = raw_input('Where should we send the email? ')
        elif len(args) == 1:
            email = args[0]
        else:
            raise CommandError('Wrong number of arguments')
        m = EmailMessage(
            subject=u'Testmail -- %s' % datetime.datetime.now(),
            body=u'This is just a stupid test mail.',
            to=[email]
            )
        m.send()


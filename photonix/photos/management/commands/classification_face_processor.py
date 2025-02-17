from django.core.management.base import BaseCommand
# Pre-load the model graphs so it doesn't have to be done for each job
from photonix.classifiers.face import run_on_photo
from photonix.photos.utils.classification import ThreadedQueueProcessor


model = None


class Command(BaseCommand):
    help = 'Runs the workers with the face detection and recognition model.'

    def run_processors(self):
        num_workers = 1
        batch_size = 64
        threaded_queue_processor = ThreadedQueueProcessor(model, 'classify.face', run_on_photo, num_workers, batch_size)
        threaded_queue_processor.run()

    def handle(self, *args, **options):
        self.run_processors()

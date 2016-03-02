import os


class ImageStore:

    LATEST = "latest.jpg"

    def __init__(self, root, config):
        self.root = root
        self.debug = config.get('DEBUG', False)

    @property
    def latest(self):
        return os.path.join(self.root, self.LATEST)

    def exists(self, image):
        image.root = self.root
        # TODO: add a way to determine if the styled image was already generated
        return os.path.isfile(image.path) and not image.style

    def create(self, image):
        if self.exists(image) and not self.debug:
            return

        image.root = self.root
        image.generate()

        try:
            os.remove(self.latest)
        except IOError:
            pass
        os.symlink(image.path, self.latest)

import os


def image_download(query, n, dest):
    """
    Saves n images from query to dest
    :param query: str
    :param n: int
    :param dest: str
    """
    if not os.path.exists(dest):
        os.mkdir(dest)

    query_results = image_query(query, n)

    for image in query_results:
        # TODO Save the image to dest/imagename.jpg (force to jpg)
        pass

    raise NotImplementedError


def image_query(query, n):
    """
    Does a search for query and returns the top n results
    :param query: str
    :return: list of images
    """
    # TODO Decide on an image format
    # TODO Decide on a search engine API
    raise NotImplementedError


if __name__ == '__main__':
    import unittest

    class TestImageQuery(unittest.TestCase):
        def setUp(self):
            pass

        def test_image_download(self):
            self.fail('Not implemented')

        def test_image_query(self):
            self.fail('Not implemented')

        def tearDown(self):
            pass

    unittest.main(verbosity=2)

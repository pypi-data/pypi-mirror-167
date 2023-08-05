import unittest
import datetime

from rss_reader.rss_reader import FeedGenerator, output_data


class RssReaderTest(unittest.TestCase):

    def test_feed_geneartion(self):

        fd = FeedGenerator("https://news.yahoo.com/rss/")
        data = fd.collect_data()

        self.assertTrue(len(data) > 0)

    def test_limit(self):

        fd = FeedGenerator("https://news.yahoo.com/rss/", limit=1)

        self.assertEqual(len(fd.collect_data()['Entries']), 1)


    def test_output_data(self):
        entries = [
            {'title': 'Test title',
             'published': datetime.datetime.now(),
             'link': 'Test link'},
             ]
        test_data = output_data({'Feed': 'Test feed', 'Entries': entries})

        self.assertEqual(type(test_data), str)

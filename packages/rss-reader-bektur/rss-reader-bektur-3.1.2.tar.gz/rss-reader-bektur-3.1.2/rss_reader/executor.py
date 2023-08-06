import feedparser
import datetime
import argparse
import json
from collections import OrderedDict

from .constants import CURRENT_VERSION
from .verbosity import method_verbosity, func_verbosity
from .cache import DBHandler


def create_args():
    '''
    Handles argparse arguments and returns "args" object
    '''

    parser = argparse.ArgumentParser()

    parser.add_argument('source', type=str, nargs='?', default='',
                        help='Receives RSS url and prints results in human-readable format')

    parser.add_argument("--limit", type=int, nargs='?', help="Set the maximum amount of output messages")

    parser.add_argument("--verbose", help="Increase output verbosity", action='store_true')
    parser.add_argument("--version", help="Show current version", action='store_true')
    parser.add_argument("--json", help="Set output format to JSON", action='store_true')
    parser.add_argument("--date", type=str, nargs='?', help="Show cached entry for given date in %Y%m%d format")

    args = parser.parse_args()

    return args


class FeedGenerator:

    '''
    Class for collecting data from received URL
    '''

    def __init__(self, url, verbose=False, limit=None):
        self.url = url
        self.limit = limit
        self.verbose = verbose

    @method_verbosity
    def __get_data(self):
        '''
        Requests data from given url via feedparser
        '''
        data = feedparser.parse(self.url)

        if hasattr(data, 'bozo_exception'):
            raise data.bozo_exception

        return data

    @method_verbosity
    def __structure_data(self, parsed_data):
        '''
        Structures received data in format of
        {
            'Feed': ...,
            'Entries: [
                {
                    'Title': ...,
                    'Date': ...,
                    'Link': ...,
                }
            ]
        }
        '''
        feed = parsed_data['feed']
        entries = parsed_data['entries']

        output_data = {}

        output_data['Feed'] = feed['title']

        if not self.limit:
            self.limit = len(entries)

        entries_data = []
        for i in range(self.limit):
            entry = OrderedDict()
            entry['Title'] = entries[i]['title']
            dto = datetime.datetime.strptime(entries[i]['published'], '%Y-%m-%dT%H:%M:%SZ')
            entry['Date'] = dto.date()
            entry['Link'] = entries[i]['link']
            entries_data.append(entry)

        output_data['Entries'] = entries_data

        return output_data

    @method_verbosity
    def collect_data(self):
        '''
        Method for client to get access to structured data
        '''
        raw_data = self.__get_data()
        structured_data = self.__structure_data(raw_data)
        db_handler = DBHandler(self.verbose)
        db_handler.write(structured_data['Entries'], structured_data['Feed'])
        return structured_data


@func_verbosity
def output_data(data, is_json=False):
    '''
    Receives dictionary of data. 
    Returns either a string or JSON formatted data for output 
    '''
    if is_json:
        return json.dumps(data)
    
    print_data = f'Feed: {data["Feed"]} \n\n'

    for entry in data['Entries']:
        for key, item in entry.items():
            print_data += f'{key}: {item} \n'
        print_data += '\n'

    return print_data


def run():
    '''
    Entrypoint function that connects functioanality of whole project
    '''
    args = create_args()

    if args.version:
        print(f'Version {CURRENT_VERSION}')

    else:

        if args.date:
            db_handler = DBHandler(verbose=args.verbose)
            data = db_handler.read_from_db(args.date)
        else:
            feed_gen = FeedGenerator(args.source, verbose=args.verbose, limit=args.limit)
            data = feed_gen.collect_data()

        print(output_data(data, args.json))

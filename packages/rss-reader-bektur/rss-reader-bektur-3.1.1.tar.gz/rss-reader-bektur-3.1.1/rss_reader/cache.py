import sqlite3
import datetime

from .verbosity import method_verbosity


def adapt_date_iso(val):
    """Adapt datetime.date to ISO 8601 date."""
    return val.isoformat()

def convert_date(val):
    """Convert ISO 8601 date to datetime.date object."""
    return datetime.date.fromisoformat(val)


class DBHandler:

    def __init__(self, verbose=False):
        self.con = sqlite3.connect('rss.db')
        self.cursor = self.con.cursor()
        self.verbose = verbose

    @method_verbosity
    def _create_table(self):
        '''
        Creates table if needed
        '''
        self.cursor.execute('CREATE TABLE IF NOT EXISTS entries (title TEXT, published date, link TEXT, feed TEXT)')

    @method_verbosity
    def write(self, entries, feed_title):
        '''
        Inserts entries info to database.
        Checks if entry is already in db by comparing titles.
        If entry is already in db, does nothing
        '''

        self._create_table()
        query = self.cursor.execute('SELECT * FROM entries')
        entries_from_db = query.fetchall()
        titles = [entry[0] for entry in entries_from_db]

        entries_to_be_written = []

        for entry in entries:
            if entry['Title'] not in titles:
                entries_to_be_written.append((entry['Title'], entry['Date'], entry['Link'], feed_title))
        if entries_to_be_written:
            self.cursor.executemany("INSERT INTO entries VALUES(?, ?, ?, ?)", entries_to_be_written)
        self.con.commit()

    @method_verbosity
    def read_from_db(self, date_string):
        '''
        Selects rows from table for given date.
        Structures and returns ready to be outputed data
        '''
        date = datetime.datetime.strptime(date_string, '%Y%m%d').date()
        query = self.cursor.execute('SELECT * FROM entries WHERE published = :date', {'date': date})
        entries = query.fetchall()

        if entries:
            feed = entries[0][3]
            output_entries = [
                {
                    'Title': entry[0],
                    'Date': entry[1],
                    'Link': entry[2]
                }
                for entry in entries
            ]

            return {'Feed': feed, 'Entries': output_entries}
        else:
            raise ValueError('No cached entry for given date')

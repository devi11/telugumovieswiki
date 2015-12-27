from bs4 import BeautifulSoup
import requests
import json

url_prefix = 'http://en.wikipedia.org/wiki/List_of_Telugu_films_of_'
movie_table_class = 'wikitable'

# Dict to keep track of column index for each field
TITLE_HEADER = 'title'
DIRECTOR_HEADER = 'director'
CAST_HEADER = 'cast'
OPENING_HEADER = 'opening'
row_indices = {
    TITLE_HEADER : 0,
    DIRECTOR_HEADER: 1,
    CAST_HEADER: 2
}


def extract_headers(row):
    """
    extracts row headers
    :param row:
    :return: {
        TITLE_HEADER : 0,
        DIRECTOR_HEADER: 1,
        CAST_HEADER: 2
    }
    Note indices are from end of list
    """
    headers = row.find_all('th')
    headers = [header.text.strip() for header in headers]
    index = 0
    header_indices = {}

    for header in reversed(headers):
        header = header.lower()
        if header == OPENING_HEADER:
            # Opening header needs special handling. Under this column there will be two sub columns.
            # One for month and one for day. So we want to skip two indexes
            index += 2
            continue
        if header == TITLE_HEADER:
            header_indices[TITLE_HEADER] = index
        elif header == DIRECTOR_HEADER:
            header_indices[DIRECTOR_HEADER] = index
        elif header == CAST_HEADER:
            header_indices[CAST_HEADER] = index
        index += 1
    return header_indices


def parse_table_row(row, year, header_indices):
    """
    Returns a dictionary of movie info from row
    :param row:
    :param header_indices: {
        TITLE_HEADER : 0,
        DIRECTOR_HEADER: 1,
        CAST_HEADER: 2
    }

    :return: {
        'name': 'xyz',
        'director': 'abc',
        'cast': ['a', 'b', 'c']
    }
    """
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]

    movie_info = {}

    # Make sure to remove empty rows
    if len(cols) > 0:
        last_index = len(cols) - 1

        # Extract movie name
        name_index = last_index - header_indices[TITLE_HEADER]
        movie_info['name'] = cols[name_index]

        # Extract director name
        director_index = last_index - header_indices[DIRECTOR_HEADER]
        movie_info['director'] = cols[director_index]

        # Extract cast
        cast_index = last_index - header_indices[CAST_HEADER]
        cast_array = cols[cast_index].split(',')
        movie_info['cast'] = cast_array

        movie_info['year'] = year
    return movie_info


def parse_table(table, year):
    data = []
    rows = table.find_all('tr')
    if len(rows) > 1:
        header_indices = extract_headers(rows[0])
        rows = rows[1:]
        for row in rows:
            data.append(parse_table_row(row, year, header_indices))
    return data


if __name__ == "__main__":
    min_year = raw_input("Enter min year: ")
    max_year = raw_input('Enter max year: ')

    min_year = int(min_year)
    max_year = int(max_year)

    if max_year < min_year:
        raise 'Max year should be more than min year'

    result = []

    for year in xrange(min_year, max_year + 1):
        url = url_prefix + str(year)
        print 'Fetch movies for year : {}, URL : {}'.format(year, url)

        try:
            r = requests.get(url)
        except Exception as e:
            print 'Error fetching the content for ' + year + ', URL: ' + url
            continue

        data = r.text
        soup = BeautifulSoup(data, 'html.parser')
        tables = soup.find_all('table', attrs={'class': movie_table_class})

        for table in tables:
            new_data = parse_table(table, year)
            result += new_data

    with open('movies.json', 'w') as f:
        json.dump(result, f)

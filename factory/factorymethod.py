import json
import xml.etree.ElementTree as et


class JSONExtractor:
    def __init__(self, filepath):
        self._dataparse = {}
        with open(filepath, encoding="utf-8", mode='r') as f:
            self._dataparse = json.load(f)

    @property
    def dataparse(self):
        return self._dataparse


class XMLExtractor:
    def __init__(self, filepath):
        self._tree = et.parse(filepath)

    @property
    def dataparse(self):
        return self._tree


def dataextractionfactory(filepath):
    if filepath.endswith("json"):
        # not creating object here , just assigning
        extractor = JSONExtractor
    elif filepath.endswith("xml"):
        extractor = XMLExtractor
    else:
        raise ValueError("Cannot extract data from file {}".format(filepath))
    return extractor(filepath)


def extract_data_from(filepath):
    factoryobj = None
    try:
        factoryobj = dataextractionfactory(filepath)
    except Exception as e:
        print(e)
    return factoryobj


def main():
    sqlite_factory = extract_data_from('data/person.sql3')
    print(sqlite_factory)

    json_factory = extract_data_from('data/movies.json')
    json_data = json_factory.dataparse
    if len(json_data) > 0:
        for data in json_data:
            movie = data['title']
            year = data['year']
            director = data['director']
            if movie and year and director:
                print("the movie {} directed by {} was released in {}".format(movie, director, year))

    xml_factory = extract_data_from('data/person.xml')
    xml_data = xml_factory.dataparse
    # using xpath to access child's child
    liars = xml_data.findall(".//person[lastName='Liar']")
    print("Number of ppl with lastname Liars are {}".format(len(liars)))
    for liar in liars:
        firstname = liar.find('.//firstName').text
        lastname = liar.find('.//lastName').text
        print("The person's firstname and lastname is {} {}".format(firstname, lastname))
        [print("Phone number : {}".format(pn.text)) for pn in liar.findall(".//phoneNumber[@type='home']")]
        print()
    print()


if __name__ == "__main__":
    main()

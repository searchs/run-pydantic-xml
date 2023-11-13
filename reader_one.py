from schemas import Collection
import pathlib

if __name__ == '__main__':
    xml_doc = pathlib.Path('./data/movie.xml').read_text()
    collection = Collection.from_xml(xml_doc)
    print(collection.genres[1])

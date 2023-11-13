from typing import List, Literal
from pydantic_xml import BaseXmlModel, attr, element


class Format(BaseXmlModel, tag='format'):
    multiple: Literal["Yes", "No"] = attr()
    # format: str = element()


class Movie(BaseXmlModel, tag="movie", arbitrary_types_allowed=True):
    # favorite: Literal["True", "False"] = attr()
    favorite: str = attr()
    title: str = attr()
    format: str = element()
    year: int = element()
    rating: str = element()
    description: str = element()


class Decade(BaseXmlModel, tag="decade"):
    years: str = attr()
    movies: List[Movie]


class Genre(BaseXmlModel, tag="genre"):
    decades: List[Decade] = element(tag="decade")
    category: str = attr(name="category")


class Collection(BaseXmlModel, tag='collection'):
    genres: List[Genre] = element(tag="genre")

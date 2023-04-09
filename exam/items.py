
from scrapy import Field, Item


class ExamItem(Item):
    """Item exercise."""

    matter = Field()
    topic = Field()
    difficulty = Field()
    enunciation = Field()
    alternatives = Field()
    multiple_choice = Field()
    enunciation_image = Field()
    image_answer = Field()
    answer = Field()
    origin = Field()
    release_date = Field()

    url = Field()

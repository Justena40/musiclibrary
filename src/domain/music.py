import json
import uuid

class Music:
    def __init__(self, **kwargs) -> None:
        self.author = kwargs["author"]
        self.genre = kwargs["genre"]
        self.title = kwargs["title"]
        self.date = kwargs["date"]
        self.uuid = str(uuid.uuid4())

    def to_dict(self):
        return self.__dict__

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Music):
            return NotImplemented

        return self.author == other.author and self.genre == other.genre and self.date == other.date and self.title == other.title

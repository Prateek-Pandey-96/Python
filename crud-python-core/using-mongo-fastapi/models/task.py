from pydantic import BaseModel

class Task(BaseModel):
    title: str
    description: str

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description
        }
class Announcement:
    id = 0
    title = ''
    text = []
    def __init__(self, id, title: str):
        self.id = id
        self.title = title

    def change_text(self, text: str):
        self.text = text

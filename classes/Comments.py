class Comment:
    def __init__(self, text: str):
        if not text.isascii():
            raise ValueError("Comments must be in English")
        self.text = text

    def display(self, index: int):
        print(f"[{index}] {self.text}")
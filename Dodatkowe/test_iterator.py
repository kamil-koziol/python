class Sentence:
    def __init__(self, sent: str):
        self.sentence = sent
        self.index = 0
        self.words = self.sentence.split()
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        else:
            index = self.index
            self.index += 1
            return self.words[index]


x = Sentence("Hello there obi wan kenobi")

for i in x:
    print(i)
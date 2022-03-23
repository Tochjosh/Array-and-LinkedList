class WordBank:

    def __init__(self, word_array):
        self.word_array = word_array

    def has_word(self, word):
        # we'll apply a front and back search
        front = 0
        back = len(self.word_array) - 1

        while front <= back:
            if self.word_array[front].lower() == word.lower() or self.word_array[back].lower() == word.lower():
                return True
            front += 1
            back -= 1
        return False




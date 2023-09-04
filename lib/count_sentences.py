#!/usr/bin/env python3
import re


class MyString:
    def __init__(self, value=''):
        self._value = value

    def get_value(self):
        return self._value

    def set_value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")

    value = property(get_value, set_value)

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        sentences = re.split(r'[.!?]', self._value)
        sentences = [sentence.strip()
                     for sentence in sentences if sentence.strip()]
        return len(sentences)

    def word_count(self):
        words = re.findall(r'\b\w+\b', self._value)
        return len(words)

    def reverse(self):
        return self._value[::-1]

    def contains_word(self, word):
        return word.lower() in self._value.lower()

    def replace_word(self, old_word, new_word):
        self._value = self._value.replace(old_word, new_word)


# Example usage:
sentence1 = MyString('This is a sentence.')
print(f"'{sentence1.get_value()}' is a sentence: {sentence1.is_sentence()}")
print(f"'{sentence1.get_value()}' is a question: {sentence1.is_question()}")
print(f"'{sentence1.get_value()}' is an exclamation: {sentence1.is_exclamation()}")

sentences = MyString('This is 1. this is 2? this is two')
sen = sentences.count_sentences()
print(f"Number of sentences: {sen}")

print(f"Word count in '{sentence1.get_value()}': {sentence1.word_count()}")
print(f"Reversed '{sentence1.get_value()}': {sentence1.reverse()}")

search_word = "sentence"
print(f"'{sentence1.get_value()}' contains '{search_word}': {sentence1.contains_word(search_word)}")

old_word = "sentence"
new_word = "phrase"
sentence1.replace_word(old_word, new_word)
print(f"Replaced '{old_word}' with '{new_word}': {sentence1.get_value()}")



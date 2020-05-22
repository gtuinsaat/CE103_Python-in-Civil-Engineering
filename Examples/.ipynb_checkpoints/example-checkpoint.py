{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "vowels = 'aeiou'\n",
    "counter = 0\n",
    "\n",
    "def word_enter():\n",
    "return input('Please write a word: ')\n",
    "\n",
    "def special(letter):\n",
    "return letter in vowels\n",
    "\n",
    "def count(counter, word):\n",
    "for letter in word:\n",
    "if special(letter):\n",
    "counter += 1\n",
    "return counter\n",
    "\n",
    "def write_screen(word):\n",
    "message = \"In the word \\\"{}\\\" there are {} vowels.\"\n",
    "print(message.format(word, count(counter, word)))\n",
    "\n",
    "def run():\n",
    "word = word_enter()\n",
    "write_screen(word)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

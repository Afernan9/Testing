import unittest
from src.Echauffment import Echauffment
import datetime
import random
import string

class TestEchauffmentMethods(unittest.TestCase):

    def test_greeting(self):
        if(datetime.datetime.now().hour < 12):
            self.assertEqual(Echauffment.greeting(), "Good morning")
        else:
            self.assertEqual(Echauffment.greeting(), "Good afternoon")

    def test_goodbye(self):
        if(datetime.datetime.now().hour < 12):
            self.assertEqual(Echauffment.goodbye(), "Have a nice day")
        else:
            self.assertEqual(Echauffment.goodbye(),  "Have a good evening")


    def test_inputProcessPalindrome(self):
        s = random.choice(string.ascii_letters)
        s = s + s[::1]
        self.assertEqual(Echauffment.process_input(s), "It's a palindrome")

    def test_inputProcessnormal(self):
        s = 'test' + random.choice(string.ascii_letters) + 'test'
        self.assertEqual(Echauffment.process_input(s), s[::-1])

if __name__ == '__main__':
    unittest.main()
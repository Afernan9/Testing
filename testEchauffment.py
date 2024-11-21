import unittest
import Echauffment
import datetime

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
        s = 'kayak'
        self.assertEqual(Echauffment.process_input(s), "It's a palindrome")

    def test_inputProcessnormal(self):
        s = 'test'
        self.assertEqual(Echauffment.process_input(s), "tset")

if __name__ == '__main__':
    unittest.main()
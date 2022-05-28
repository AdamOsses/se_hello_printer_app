from hello_world.formater import plain_text_upper_case
import unittest # biblioteka do testowania w Pythonie


class TestFormater(unittest.TestCase):
    def test_plain_uppercase(self):
        r = plain_text_upper_case("wwww", "EEEMSG")
        name = r.split(" ")[0]
        msg = r.split(" ")[1]
        self.assertTrue(name.isupper()) # sprawdzenie czy to prawda assertTrue
        self.assertTrue(msg.isupper())

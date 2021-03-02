import unittest
from ah_yacc import parse


class TestAHYacc(unittest.TestCase):
    def test_yacc_1(self):
        input_str = "red, blue, white, purple; dead none; skip; dead blue; red, purple doubt white; eject white;"
        participants, meetings_info = parse(input_str)
        self.assertEquals(len(participants), 4)
        self.assertEquals(participants[0], "red")
        self.assertEquals(participants[-1], "purple")
        self.assertEquals(len(meetings_info), 2)
        self.assertIsNone(meetings_info[0].dead_info)
        self.assertIsNone(meetings_info[0].testimonies)
        self.assertIsNone(meetings_info[0].conclusion)
        self.assertEquals(meetings_info[1].dead_info, "blue")
        self.assertEquals(meetings_info[1].testimonies[0].testimony_type, "doubt")
        self.assertEquals(
            meetings_info[1].testimonies[0].member_from, ["red", "purple"]
        )
        self.assertEquals(meetings_info[1].testimonies[0].member_to, ["white"])
        self.assertEquals(meetings_info[1].conclusion, "white")

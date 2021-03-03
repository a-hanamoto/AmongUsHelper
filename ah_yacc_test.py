import unittest
from ah_yacc import parse


class TestAHYacc(unittest.TestCase):
    def test_yacc_1(self):
        input_str = "red, blue, white, purple; dead none; skip; dead blue; red, purple doubt white; eject white;"
        participants, meetings_info, _ = parse(input_str)
        self.assertEqual(len(participants), 4)
        self.assertEqual(participants[0], "red")
        self.assertEqual(participants[-1], "purple")
        self.assertEqual(len(meetings_info), 2)
        self.assertIsNone(meetings_info[0].dead_info)
        self.assertIsNone(meetings_info[0].testimonies)
        self.assertIsNone(meetings_info[0].conclusion)
        self.assertEqual(meetings_info[1].dead_info, "blue")
        self.assertEqual(meetings_info[1].testimonies[0].testimony_type, "doubt")
        self.assertEqual(
            meetings_info[1].testimonies[0].member_from, ["red", "purple"]
        )
        self.assertEqual(meetings_info[1].testimonies[0].member_to, ["white"])
        self.assertEqual(meetings_info[1].conclusion, "white")

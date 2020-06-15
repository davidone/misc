import wrap
import unittest


class MainTescoAddon(unittest.TestCase):
    def test_process_tesco(self):
        ret_assert = (
            "2020-07-02T19:00:00.000Z - "
            "2020-07-02T20:00:00.000Z || "
            "2020-07-01T19:00:00.000Z - "
            "2020-07-01T20:00:00.000Z"
        )
        tesco_list = [
            (
                "  { start: 2020-06-30T18:00:00.000Z, "
                "end: 2020-06-30T19:00:00.000Z },"
            ),
            (
                "  { start: 2020-07-01T19:00:00.000Z, "
                "end: 2020-07-01T20:00:00.000Z },",
            ),
            ("  { start: 2020-07-02T19:00:00.000Z, " "end: 2020-07-02T20:00:00.000Z }"),
        ]
        days_list = ["2020-07-01", "2020-07-02"]
        ret_value = wrap.process_tesco(tesco_list, days_list)
        self.assertEqual(ret_value, ret_assert)

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from parse_name import parse_name


def test_parse_name_returns_romanized_strings_and_counts():
    data = [["タイトル", "ジャンル"]]
    expected = [["taitoru", 7, "janru", 5]]
    assert parse_name(data) == expected

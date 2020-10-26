from app.loader import import_records
import pytest

def test_import_records():
    records = import_records("tests/dataset/*.csv")
    user_records = records['user_records']
    ad_records = records['ad_records']

    assert(len(user_records)) == 3
    assert(len(ad_records)) == 5

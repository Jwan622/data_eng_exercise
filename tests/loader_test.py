from app.loader import import_records


def test_import_records():
    records = import_records("tests/dataset/*.csv")
    user_records = records['user_records']
    ad_records = records['ad_records']
    expected_user_records = [('event1', 'user1', 'phone1', 'drinking', 'NULL', '2019-07-01 18:42:45.151967'), ('event2', 'user2', 'phone2', 'drinking', 'Yes', '2019-07-01 18:42:45.151987'), ('event3', 'user3', 'phone3', 'sex', 'F', '2019-07-01 18:42:45.152005'), ('event4', 'user4', 'phone4', 'drinking', 'Yes', '2019-07-01 18:42:46.151987'), ('event5', 'user5', 'phone5', 'drinking', 'No', '2019-07-01 18:42:47.151987')]
    expected_ad_records = [('event1', 'phone1', '2', 'Spotify', 'Bottom', '10', '2019-07-01 18:42:45.151950'), ('event2', 'phone2', '1', 'Spotify', 'Center', '11', '2019-07-01 18:42:46.151981'), ('event3', 'phone3', '3', 'Facebook', 'Middle', '12', '2019-07-01 18:42:47.151981'), ('c9533e2038428ce2fd146f097c940cf5', '50c97ef8cedae6980246a082b04d1c4b', '6', 'Facebook', 'Bottom', '1906', '2019-07-03 18:42:45.197143'), ('b96b8f7d1501f7dce3a099ba7fa05f95', 'ba3aacfecf27077b147317f1edd4e6b0', '17', 'Instagram', 'Right', '2225', '2019-07-03 18:42:45.197160')]

    assert(user_records) == expected_user_records
    assert(ad_records) == expected_ad_records


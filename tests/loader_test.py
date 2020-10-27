from app.loader import import_records

def test_import_records():
    records = import_records("tests/dataset/*.csv")
    user_records = records['user_records']
    ad_records = records['ad_records']
    expected_user_records = [
        {
            'event_id': 'event1',
            'user_id': 'user1',
            'phone_id': 'phone1',
            'property': 'drinking',
            'value': 'NULL',
            'event_ts': '2019-07-01 18:42:45.151967'
        },
        {
            'event_id': 'event2',
            'user_id': 'user2',
            'phone_id': 'phone2',
            'property': 'drinking',
            'value': 'Yes',
            'event_ts': '2019-07-01 18:42:45.151987'
        },
        {
            'event_id': 'event3',
            'user_id': 'user3',
            'phone_id': 'phone3',
            'property': 'sex',
            'value': 'F',
            'event_ts': '2019-07-01 18:42:45.152005'
        },
        {
            'event_id': 'event4',
            'user_id': 'user4',
            'phone_id': 'phone4',
            'property': 'drinking',
            'value': 'Yes',
            'event_ts': '2019-07-01 18:42:46.151987'
        },
        {
            'event_id': 'event5',
            'user_id': 'user5',
            'phone_id': 'phone5',
            'property': 'drinking',
            'value': 'No',
            'event_ts': '2019-07-01 18:42:47.151987'
        }
    ]
    expected_ad_records = [
        {
            'event_id': 'event1',
            'phone_id': 'phone1',
            'ad_id': '2',
            'provider': 'Spotify',
            'placement': 'Bottom',
            'length': '10',
            'event_ts': '2019-07-01 18:42:45.151950'
        },
        {
            'event_id': 'event2',
            'phone_id': 'phone2',
            'ad_id': '1',
            'provider': 'Spotify',
            'placement': 'Center',
            'length': '11',
            'event_ts': '2019-07-01 18:42:46.151981'
        },
        {
            'event_id': 'event3',
            'phone_id': 'phone3',
            'ad_id': '3',
            'provider': 'Facebook',
            'placement': 'Middle',
            'length': '12',
            'event_ts': '2019-07-01 18:42:47.151981'
        },
        {
            'ad_id': '6',
            'event_id': 'c9533e2038428ce2fd146f097c940cf5',
            'event_ts': '2019-07-03 18:42:45.197143',
            'length': '1906',
            'phone_id': '50c97ef8cedae6980246a082b04d1c4b',
            'placement': 'Bottom',
            'provider': 'Facebook'
        },
        {
            'ad_id': '17',
            'event_id': 'b96b8f7d1501f7dce3a099ba7fa05f95',
            'event_ts': '2019-07-03 18:42:45.197160',
            'length': '2225',
            'phone_id': 'ba3aacfecf27077b147317f1edd4e6b0',
            'placement': 'Right',
            'provider': 'Instagram'
        },
    ]

    assert(user_records) == expected_user_records
    assert(ad_records) == expected_ad_records


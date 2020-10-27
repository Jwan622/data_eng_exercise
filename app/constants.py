MARKETING_FILE_PREFIX = "marketing"
USER_FILE_PREFIX = "user"
USER_RECORDS_KEY = "user_records"
AD_RECORDS_KEY = "ad_records"
AD_TABLE_NAME = "ad_events"
USER_TABLE_NAME = "user_events"
RECORD_KEY_TO_TABLE_NAME = {
    USER_RECORDS_KEY: USER_TABLE_NAME,
    AD_RECORDS_KEY: AD_TABLE_NAME
}
RECORD_KEY_TO_COLUMNS = {
    AD_RECORDS_KEY: '(event_id, phone_id, ad_id, provider, placement, length, event_ts)',
    USER_RECORDS_KEY: '(event_id, user_id, phone_id, property, value, event_ts)'
}
FIELD_NAMES = {
    USER_RECORDS_KEY: ["event_id", "user_id", "phone_id", "property", "value", "event_ts"],
    AD_RECORDS_KEY: ["event_id", "phone_id", "ad_id", "provider", "placement", "length", "event_ts"]
}

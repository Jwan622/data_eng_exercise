CREATE TABLE ad_events (
    id serial PRIMARY KEY,
    event_id varchar(255) NOT NULL,
    phone_id varchar(255),
    ad_id int,
    provider varchar(255),
    placement varchar(255),
    length int,
    event_ts date
);

CREATE TABLE user_events (
    id serial PRIMARY KEY,
    event_id varchar(255) NOT NULL,
    user_id varchar(255),
    phone_id varchar(255),
    property varchar(255),
    value varchar(80),
    event_ts date
);

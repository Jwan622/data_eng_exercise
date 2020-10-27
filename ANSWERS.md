**Data Analysis**

1\. What is the number of unique users?
```sql
SELECT COUNT(DISTINCT user_id) AS NumberOfUniqueUsers 
    FROM user_events;
```
__answer:__ 
> 2903

2\. Who are the marketing ad providers?
```sql
select DISTINCT provider from ad_events;
```
__answer:__
> Instagram Facebook Snapchat Spotify 

3\. Which user property is changed the most frequently?
```sql
SELECT property
    FROM user_events
    GROUP BY property
    ORDER BY COUNT(*) DESC
    LIMIT 1;
```
__answer:__ 
>  drinking

4\. How many users were shown a Snapchat ad on July 3rd, 2019?
```sql
SELECT count(DISTINCT user_id) 
    FROM user_events users join ad_events ads on users.phone_id=ads.phone_id
    WHERE ads.provider='Snapchat'
        AND ads.event_ts='2019-07-03';
```
__answer:__ 
> 236

5\. Which ad was shown the most to users who identify as moderates?
```sql
select ad_id, COUNT(*)
    FROM (select DISTINCT user_id, phone_id
    FROM user_events users
    WHERE property='politics'
        AND value='Moderate') moderate_users JOIN ad_events ads on moderate_users.phone_id=ads.phone_id
    GROUP BY ad_id
    ORDER BY COUNT(*) DESC
    LIMIT 1;
```
__some quick analysis:__
```sql
select DISTINCT user_id
    FROM user_events users
    WHERE property='politics'
        AND value='Moderate'
```

The above query represents all users who are presently moderate. And of these people, join that list of users to ads, 
then count the most common ad. 

__Possible problem:__
It is possible that some people returned from the query were conservative or liberal 
previously before switching to moderate and so... if they were shown ads at that previous time, it's not captured by this query.

__answer:__ 
> Ad 4 was shown 76 times

6\. What are the top 5 ads? Explain how you arrived at that conclusion.

I'll give a few different answers and what they mean. It all depends on the word "top".

So this query:
```sql
SELECT ad_id, COUNT(*)
    FROM ad_events
    GROUP BY ad_id
    ORDER BY COUNT(*) DESC
    LIMIT 5;
```
will return this:

```text
 ad_id | count
-------+-------
     1 |   745
     4 |   731
     2 |   689
     3 |   673
     0 |   673
```

which will show the ad with the most events/the most shown ad. That's one definition of top.

This other query:

```sql
SELECT ad_id, 
    COUNT(*) as numberOfTimesAdShown, 
    COUNT(DISTINCT phone_id) as numberOfUniqueUsersShown
    FROM ad_events
    GROUP BY ad_id
    ORDER BY COUNT(*) DESC
    LIMIT 5;
```
which returns this:

```text
ad_id | numberoftimesadshown | numberofuniqueusersshown
-------+----------------------+--------------------------
     1 |                  745 |                      639
     4 |                  731 |                      635
     2 |                  689 |                      612
     3 |                  673 |                      592
     0 |                  673 |                      605
```

has the same data but it also shows how many users it was shown to, again ordered by number of times the ad was shown.

The query below shows similar info but ordered by the number of unique users it was shown to, which might be anotther metric of how "effective" an ad is.
```sql
SELECT ad_id, 
    COUNT(*) as numberOfTimesAdShown, 
    COUNT(DISTINCT phone_id) as numberOfUniqueUsersShown
    FROM ad_events
    GROUP BY ad_id
    ORDER BY COUNT(DISTINCT phone_id) DESC
    LIMIT 5;
```

Lastly, this query:
```sql
SELECT ad_id, 
    COUNT(*) as numberOfTimesAdShown, 
    COUNT(DISTINCT phone_id) as numberOfUniqueUsersShown,
    AVG(length) as avg_length
    FROM ad_events
    GROUP BY ad_id
    ORDER BY 4 DESC
    LIMIT 5;
```
returns:

```text
ad_id | numberoftimesadshown | numberofuniqueusersshown |      avg_length
-------+----------------------+--------------------------+-----------------------
    14 |                  141 |                      139 | 1280.3687943262411348
     0 |                  673 |                      605 | 1251.2823179791976226
    11 |                  157 |                      154 | 1240.3312101910828025
    20 |                   97 |                       92 | 1237.1649484536082474
    12 |                  173 |                      166 | 1232.9017341040462428
```
So the aboe query determins a top ad by the length of the ad shown. Presumably it's how long the ad was viewed.




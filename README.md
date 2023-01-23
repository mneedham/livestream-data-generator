# Live stream data generator

This project generates data that simulates a bunch of live stream events and people joining/leaving each event.

## Installation

```bash
pip install -r requirements.txt
```

## Running the generator

The following command generates events every second for 1,000 users, 1000 events, with event length between 60-180 seconds, and attendees joining events immediately.

```bash
python loop.py \
  --timeout 1 \
  --users 1000 \
  --events 100 \
  --max-start-delay 0 \
  --min-event-length 60 \
  --max-event-length 180
```
 
The output should look like this:

```json
{"eventTime": "2023-01-23T10:15:24.089789", "eventId": "89653462-d58c-4751-974b-cc94d9fa9a11", "userId": "cf29d9e5-4f52-43cf-99c6-b6138ae612eb", "name": "Beverly Kelley", "lat": "51.5085", "lng": "-0.1257", "city": "London", "region": "England", "action": "Join"}
{"eventTime": "2023-01-23T10:15:24.048042", "eventId": "3bf77680-7664-44a2-b5eb-7281fb759999", "userId": "31ab115f-b7a4-48a6-a282-5e5a3c15ddf0", "name": "Jeffery Adams", "lat": "32.5530", "lng": "-92.0422", "city": "Monroe", "region": "Louisiana", "action": "Join"}
{"eventTime": "2023-01-23T10:15:24.033714", "eventId": "0283e8e6-14a7-4d8e-8aab-5d40d38eb52d", "userId": "0acad44c-2545-4c81-bd3f-33385d21160f", "name": "Alexander Fuller", "lat": "43.2501", "lng": "-79.8496", "city": "Hamilton", "region": "Ontario", "action": "Join"}
{"eventTime": "2023-01-23T10:15:23.979862", "eventId": "bf061b6c-b03d-43d7-9d04-f4f8c71a9ab0", "userId": "0a9f8527-a2b4-4c5f-b82b-2a3930182c62", "name": "Julie Grant", "lat": "35.6910", "lng": "139.7679", "city": "Tokyo", "region": "Tokyo", "action": "Join"}
{"eventTime": "2023-01-23T10:15:24.075753", "eventId": "868320eb-96b2-496f-af72-9cd83d9726c0", "userId": "fc20e945-f4ce-4c71-9a55-8f7253583c1c", "name": "Natalie Martinez", "lat": "39.9690", "lng": "-83.0114", "city": "Columbus", "region": "Ohio", "action": "Join"}
```

## Ingesting into Apache Kafka

If you want to ingest those events into a data streaming platform like Kafka, you can do so using the [jq](https://stedolan.github.io/jq/) and [kcat](https://docs.confluent.io/platform/current/app-development/kafkacat-usage.html) command line tools:

```bash
python loop.py \
  --timeout 1 \
  --users 1000 \
  --events 100 \
  --max-start-delay 0 \
  --min-event-length 60 \
  --max-event-length 180 |
jq -cr --arg sep 😊 '[.eventId, tostring] | join($sep)' |
kcat -P -b localhost:9092 -t events -K😊
```

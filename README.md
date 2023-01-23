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

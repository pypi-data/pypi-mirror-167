# Open Telemetry GCP PubSub Instrumentation for Python

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/tommbee/opentelemetry-python-instrumentation-pubsub/tree/main.svg?style=shield)](https://dl.circleci.com/status-badge/redirect/gh/tommbee/opentelemetry-python-instrumentation-pubsub/tree/main)
[![PyPi version](https://img.shields.io/pypi/v/opentelemetry-instrumentation-pubsub.svg)](https://pypi.org/project/opentelemetry-instrumentation-pubsub/)

This package provides automatic instrumentation for the [`google-cloud-pubsub`](https://pypi.org/project/google-cloud-pubsub/) client library.

## Installation
```bash
pip install opentelemetry-instrumentation-pubsub
```

## Usage
Initiate the instrumentor after configuring your [Open Telemetry](https://opentelemetry.io/docs/instrumentation/python/manual/) trace provider.

```python
from google.cloud import pubsub_v1
from pubsub_opentelemetry import PubSubInstrumentationProvider


# Instrument PubSub
PubSubInstrumentationProvider().instrument()

# Publish creates a span with PubSub specific attributes
with pubsub_v1.PublisherClient() as publisher:
    publisher.publish(topic_name, b'My first message!')

# Subscribe propagates the context from the received message
with pubsub_v1.SubscriberClient() as subscriber:
    subscriber.subscribe(subscription_name, callback)
```
---

## Development

Install dependencies:
```bash
make install
```

Run lint checks:
```bash
make lint
```

Run unit tests:
```bash
make test
```

Run tests against supported Python versions (using tox):
```bash
make tox
```

[License](LICENSE)

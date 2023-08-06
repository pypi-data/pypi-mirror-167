import wrapt
from google.cloud.pubsub_v1 import PublisherClient, SubscriberClient

from pubsub_opentelemetry import PubSubInstrumentationProvider


class TestPubSubInstrumentationProvider:
    def test_instrument(self) -> None:
        PubSubInstrumentationProvider().instrument()
        assert isinstance(PublisherClient.publish, wrapt.BoundFunctionWrapper)
        assert isinstance(SubscriberClient.subscribe, wrapt.BoundFunctionWrapper)

    def test_uninstrument(self) -> None:
        PubSubInstrumentationProvider().instrument()
        PubSubInstrumentationProvider().uninstrument()
        assert not isinstance(PublisherClient.publish, wrapt.BoundFunctionWrapper)
        assert not isinstance(SubscriberClient.subscribe, wrapt.BoundFunctionWrapper)

from opentelemetry import trace

from pubsub_opentelemetry.publisher_decorator import PublisherDecorator


class TestPublisherDecorator:
    def test_decorate(self, mocker) -> None:
        result = mocker.Mock
        func = mocker.Mock(return_value=result)
        tracer = trace.get_tracer(__name__)
        spy = mocker.spy(tracer, 'start_as_current_span')

        decorated = PublisherDecorator(tracer).decorate(func)
        actual = decorated('topic', b'message data')

        assert func.called
        assert actual == result
        spy.assert_called_once_with(
            'topic send',
            kind=trace.SpanKind.PRODUCER,
            attributes={
                'messaging.system': 'pubsub',
                'messaging.protocol': 'pubsub',
                'messaging.destination': 'topic',
                'messaging.destination_kind': 'topic',
                'messaging.message_payload_size_bytes': '12',
                'messaging.operation': 'send',
            },
        )

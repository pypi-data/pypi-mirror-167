from opentelemetry import propagate, trace

from pubsub_opentelemetry.subscriber_decorator import SubscriberDecorator


class TestSubscriberDecorator:
    def test_decorate(self, mocker):
        mocker.patch('opentelemetry.propagate.extract')
        propagate.extract.return_value = {'foo': 'bar'}

        message = mocker.Mock
        message.message_id = '001'
        message.attributes = {}
        message.data = b'123'

        mock_callback = mocker.Mock(return_value=message)

        def func(subscription: str, callback):
            assert subscription == 'subscription'
            return callback(message)

        tracer = trace.get_tracer(__name__)
        spy = mocker.spy(tracer, 'start_span')

        decorated = SubscriberDecorator(tracer).decorate(func)
        actual = decorated('subscription', mock_callback)
        assert actual == message
        assert mock_callback.called
        spy.assert_called_once_with(
            'subscription process',
            kind=trace.SpanKind.CONSUMER,
            attributes={
                'messaging.system': 'pubsub',
                'messaging.protocol': 'pubsub',
                'messaging.message_id': '001',
                'messaging.destination': 'subscription',
                'messaging.destination_kind': 'subscription',
                'messaging.message_payload_size_bytes': 3,
                'messaging.operation': 'process',
            },
            context={'foo': 'bar'},
        )

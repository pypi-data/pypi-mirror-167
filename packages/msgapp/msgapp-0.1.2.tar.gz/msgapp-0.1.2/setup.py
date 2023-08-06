# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['msgapp', 'msgapp.parsers', 'msgapp.producers']

package_data = \
{'': ['*']}

install_requires = \
['anyio>=3.6.1']

extras_require = \
{':python_version < "3.8"': ['typing-extensions>=4.3.0,<5.0.0'],
 'dev': ['pydantic>=1.9.1', 'google-cloud-pubsub>=2.13.4'],
 'json': ['pydantic>=1.9.1'],
 'pubsub': ['google-cloud-pubsub>=2.13.4']}

setup_kwargs = {
    'name': 'msgapp',
    'version': '0.1.2',
    'description': 'Declarative message processing applications',
    'long_description': '# msgapp: declarative message driven applications\n\n`msgapp` helps you write event consuming applications with minimal boilerplate.\nIt abstracts away some of the fiddly details of dealing with messaging queues like acks, deadlines and parsing.\nThe design is focused on flexibility and testability, offering the ability to swap out event backends (currently only PubSub) and support multiple parsers (only JSON via Pydantic is supplied out of the box for now).\n\n## Examples\n\n### Pydantic + PubSub\n\n```python\nimport anyio\nfrom pydantic import BaseModel\nfrom msgapp import App\nfrom msgapp.producers.pubsub import PubSubQueue\nfrom msgapp.parsers.json import PydanticParserFactory\n\nclass MyModel(BaseModel):\n    foo: str\n    baz: int\n\nasync def handler(model: MyModel) -> None:\n    # do something with the model\n    print(model)\n    # return to ack/consume the model\n    # raise an exception to signal an error\n    # and let the queue handle redelivery\n\napp = App(\n    handler,\n    producer=PubSubQueue(subscription="projects/demo/subscriptions/foo-bar"),\n    parser=PydanticParserFactory(),\n)\n\nanyio.run(app.run)\n```\n\n### Redis Streams + Pydantic\n\nWe do not include a Redis implementation simply because there are many ways that redis can be used for messaging. For example, you may use Redis\' PubSub functionality for fire and forget messaging or Streams for reliable Kafka-like operation.\n\nBelow is an example implementation using Redis streams.\nWhile this may not be exactly the implementation you want, it should give you some idea of how to write a Redis producer.\n\n```python\nfrom contextlib import asynccontextmanager\nfrom dataclasses import dataclass\nfrom typing import (\n    Any,\n    AsyncContextManager,\n    AsyncIterator,\n    Mapping,\n    Optional,\n    Sequence,\n    Tuple,\n)\n\nfrom redis.asyncio import Redis\nfrom redis.exceptions import ResponseError\n\nfrom msgapp._producer import Producer\n\n\n@dataclass(frozen=True)\nclass RedisMessage:\n    payload: Mapping[bytes, bytes]\n    id: bytes\n\n\nclass RedisWrappedEnvelope:\n    def __init__(self, message: RedisMessage, body: bytes) -> None:\n        self._message = message\n        self._body = body\n\n    @property\n    def body(self) -> bytes:\n        return self._body\n\n    @property\n    def message(self) -> RedisMessage:\n        return self._message\n\n\nclass RedisProducer(Producer[Any]):\n    def __init__(\n        self,\n        client: "Redis[Any]",\n        stream: str,\n        group: str,\n        message_key: bytes,\n        consumer_name: str,\n        batch_size: int = 10,\n        poll_interval: int = 30,\n    ) -> None:\n        self._client = client\n        self._stream = stream\n        self._group = group\n        self._batch_size = batch_size\n        self._poll_interval = poll_interval\n        self._message_key = message_key\n        self._consumer_name = consumer_name\n\n    async def pull(self) -> AsyncIterator[AsyncContextManager[RedisWrappedEnvelope]]:\n        try:\n            await self._client.xgroup_create(\n                name=self._stream, groupname=self._group, mkstream=True\n            )\n        except ResponseError as e:\n            if "Consumer Group name already exists" in e.args[0]:\n                pass\n            else:\n                raise\n        last_id: Optional[bytes] = None\n        items: Optional[\n            Sequence[Tuple[str, Sequence[Tuple[bytes, Mapping[bytes, bytes]]]]]\n        ] = None\n        while True:\n            items = await self._client.xreadgroup(\n                groupname=self._group,\n                consumername=self._consumer_name,\n                streams={self._stream: last_id or ">"},\n                block=1,\n                count=1,\n            )\n            if not items:\n                continue\n            stream_items = next(iter(items))\n            if len(stream_items[1]) == 0:\n                last_id = None\n                continue\n            _, stream_messages = stream_items\n            for message_id, values in stream_messages:\n                last_id = message_id\n\n                wrapped_msg = RedisMessage(payload=values, id=message_id)\n                wrapped_envelope = RedisWrappedEnvelope(\n                    wrapped_msg, values[self._message_key]\n                )\n\n                @asynccontextmanager\n                async def msg_wrapper(\n                    envelope: RedisWrappedEnvelope = wrapped_envelope,\n                ) -> AsyncIterator[RedisWrappedEnvelope]:\n                    yield envelope\n                    await self._client.xack(  # type: ignore\n                        self._stream, self._group, envelope.message.id\n                    )\n\n                yield msg_wrapper()\n\n\nif __name__ == "__main__":\n    import anyio\n    from pydantic import BaseModel\n\n    from msgapp import App\n    from msgapp.parsers.json import PydanticParserFactory\n\n    class MyModel(BaseModel):\n        foo: str\n\n    async def handler(message: MyModel) -> None:\n        print(repr(message))\n\n    stream = "mystream"  # str(uuid4())\n\n    async def main() -> None:\n        client = Redis.from_url("redis://localhost")\n        producer = RedisProducer(client, stream, "mygroup", b"message", "consumer")\n\n        app = App(handler, parser=PydanticParserFactory(), producer=producer)\n\n        async with anyio.create_task_group() as tg:\n            tg.start_soon(app.run)\n            await client.xadd(stream, {b"message": b\'{"foo": "bar"}\'})\n            await client.xadd(stream, {b"message": b\'{"foo": "baz"}\'})\n            await anyio.sleep(1)\n            tg.cancel_scope.cancel()\n\n    anyio.run(main)\n```\n\nSee this release on GitHub: [v0.1.2](https://github.com/adriangb/msgapp/releases/tag/0.1.2)\n',
    'author': 'Adrian Garcia Badaracco',
    'author_email': 'dev@adriangb.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/adriangb/msgapp',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)

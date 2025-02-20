# coding: UTF-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@datetime: 2024-07-17 10:42:19 UTC+08:00
"""

import json
import warnings
from typing import Dict, Union, Tuple, Sequence

from elasticsearch import Elasticsearch
from opensearchpy import OpenSearch

from fairylandfuture.exceptions.es import ElasticSearchExecutionException
from fairylandfuture.exceptions.messages.es import ElasticSearchExceptMessage

warnings.filterwarnings("ignore")


class ElasticSearchOperator:

    def __init__(self, client: Union[Elasticsearch, OpenSearch]):
        self.__client = client

    @property
    def client(self):
        return self.__client

    @property
    def indices(self) -> Tuple[str, ...]:
        indices: Dict[str, ...] = self.client.indices.get("*")
        return tuple([index for index in indices.keys()])

    def simple_search(self, index, dsl) -> Tuple[int, Sequence[Dict[str, ...]]]:
        data: Dict[str, ...] = self.client.search(index=index, body=dsl)
        if data.get("timed_out"):
            raise ElasticSearchExecutionException(ElasticSearchExceptMessage.TIMEOUT)

        total: int = data.get("hits").get("total").get("value")
        hits: List[Dict[str, ...]] = data.get("hits").get("hits")

        return total, tuple(hits)

    def run(self):
        self.client.update_by_query(index="asd", body={}, conflicts="proceed")


if __name__ == '__main__':
    client = OpenSearch("http://10.65.66.213:19399", meta_header=False, verify_certs=False)
    es_operator = ElasticSearchOperator(client)

    index = "internal_isop_event*"
    query = {
        "query": {
            "bool": {
                "must": [
                    {
                        "nested": {
                            "path": "destination",
                            "query": {
                                "bool": {
                                    "must": [
                                        {
                                            "term": {
                                                "destination.ip": "23.12.104.144"
                                            }
                                        }
                                    ]
                                }
                            }
                        }
                    }
                ]
            }
        }
    }
    # data = client.search(query, "internal_isop_event*")

    total, hits = es_operator.simple_search(index, query)
    print(hits)


    # print(data)

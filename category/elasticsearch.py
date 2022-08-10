from csv import reader
import json
from collections import deque
import elasticsearch7
from elasticsearch7 import helpers
import warnings

def readline(all_data):
    # 수정 : jqeury에서 마지막 빈데이터 전송하는 부분 처리 필요!!(현재는 파이썬 코드에서 처리)
    for line in all_data[:-1]:
        yield line


def push_elasticsearch(data):
    es = elasticsearch7.Elasticsearch(["http://localhost:9200"])

    # tourist => web에서 인덱스 명 설정
    es.indices.delete(index="test", ignore=404)
    deque(helpers.parallel_bulk(es, readline(data), index="test"), maxlen=0)
    es.indices.refresh()


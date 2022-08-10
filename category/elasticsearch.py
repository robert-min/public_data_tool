from csv import reader
import json
from collections import deque
import elasticsearch7
from elasticsearch7 import helpers

def readline(count, csv_data):
    for line in csv_data:
        i = 0
        line_data = {}
        while i != count:
            line_data[header[i]] = line[i]
            i += 1
        yield line_data

with open("./test_file/강원도_동해시_관광객수 정보_10_21_2021.csv", "r") as file:
    csv_reader = reader(file)
    header = next(csv_reader)

    es = elasticsearch7.Elasticsearch(["http://localhost:9200"])

    #
    # tourist => web에서 인덱스 명 설정
    es.indices.delete(index="tourist", ignore=404)
    deque(helpers.parallel_bulk(es, readline(len(header), csv_reader), index="tourist"), maxlen=0)
    es.indices.refresh()
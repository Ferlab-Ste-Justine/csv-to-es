from elasticsearch import Elasticsearch


def get_es(conf) -> Elasticsearch:
    return Elasticsearch(
        hosts=conf['elasticsearch']['host'],
        scheme=conf['elasticsearch']['scheme'],
        port=conf['elasticsearch']['port'],
    )

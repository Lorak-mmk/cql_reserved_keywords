#!/usr/bin/env python
import re
from collections import defaultdict
from cassandra.cluster import Cluster
from cassandra.protocol import SyntaxException

def flatten(xss):
    return [x for xs in xss for x in xs]

def classify_keywords(all_keywords_str, unreserved_keywords_str):
    all_keywords_pairs = re.split('[:;]', all_keywords_str.strip())

    all_keywords = defaultdict(lambda : [])
    for i in range(0, len(all_keywords_pairs) & -2, 2):
        key = all_keywords_pairs[i].strip()
        value = all_keywords_pairs[i + 1].strip().replace(' ', '').replace('\'', '').replace('\n', '').lower()
        if value.startswith('('):
            split_values = value[1:-1].split('|')
            value = flatten(map(lambda k : all_keywords[k.upper()] if k.startswith('k_') else [k], split_values))
        else:
            value = [value]
        all_keywords[key] += value

    unreserved_keywords = set(re.findall('K_[A-Z_]+', unreserved_keywords_str))
    reserved = []
    unreserved = []
    for keyword, keyword_texts in all_keywords.items():
        if keyword in unreserved_keywords:
            unreserved += keyword_texts
        else:
            reserved += keyword_texts
    for unreserved_keyword in unreserved_keywords:
        if unreserved_keyword not in all_keywords:
            raise "Error: unknown keyword in unreserved keywords"
    return (reserved, unreserved)

def is_keyword_reserved(session, keyword):
    queries = [
        f'CREATE TABLE mykeyspace.{keyword} (a INT PRIMARY KEY);',
        f'SELECT * FROM {keyword};',
        f'INSERT INTO {keyword}(a, b, c) VALUES (1, 2, 3)'
    ]
    for q in queries:
        try:
            print(session.execute(q))
        except SyntaxException as e:
            #print(e)
            return True
        except:
            pass
    return False

def get_reserved(data):
    (reserved, unreserved) = classify_keywords(data.case_insensitive_keywords, data.unreserved_keywords)
    cluster = Cluster([data.host], port=data.port)
    session = cluster.connect()

    really_reserved = set()
    for k in sorted(reserved):
        is_really_reserved = is_keyword_reserved(session, k)
        if is_really_reserved:
            really_reserved.add(k)
        else:
            raise f'Keyword falsely reserved: {k}'

    really_unreserved = set()
    for k in sorted(unreserved):
        is_really_reserved = is_keyword_reserved(session, k)
        if not is_really_reserved:
            really_unreserved.add(k)
        else:
            raise f'Keyword falsely unreserved: {k}'
            
    
    return really_reserved, really_unreserved



import data_scylla
import data_cassandra


reserved_scylla, unreserved_scylla = get_reserved(data_scylla)
reserved_cassandra, unreserved_cassandra = get_reserved(data_cassandra)
print("Reserved:\n")
for k in sorted(reserved_scylla | reserved_cassandra):
    print(k)
print("\nUnreserved:\n")
for k in sorted(unreserved_scylla & unreserved_cassandra):
    print(k)

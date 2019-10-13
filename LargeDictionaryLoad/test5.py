# Use a [Trie](https://github.com/pytries/marisa-trie)

import gc
import os
import marisa_trie
import pathlib
import psutil
import string
import uuid
from datetime import datetime as dt

### edit me - start
key_column = 1
value_column = 2
source_file_name = 'd:/test/source_1.csv'
sample_file_name = 'd:/test/sample_1.csv'
### edit me - end

source_file_name = pathlib.Path(source_file_name)
sample_file_name = pathlib.Path(sample_file_name)

print('Loading dictionary...')
t1 = dt.utcnow()
def gen_keys(source_file_name):
    with open(source_file_name, 'r', encoding = 'utf-8', newline = '') as source_file:
        for line in source_file:
            yield line.strip().split(',')[key_column]
mydict = marisa_trie.Trie(gen_keys(source_file_name))
with open(source_file_name, 'r', encoding = 'utf-8', newline = '') as source_file:
    values = [line.strip().split(',')[value_column] for line in source_file.readlines()]
print(dt.utcnow() - t1)

gc.collect()
pid = os.getpid()
py = psutil.Process(pid)
print('{ram} MB used so far'.format(ram = int(py.memory_info().vms/1024/1024)))

print('Loading real keys (hits)...')
t1 = dt.utcnow()
with open(sample_file_name, 'r', encoding = 'utf-8', newline = '') as sample_file:            
    hits = [line.strip() for line in sample_file.readlines()]
print(dt.utcnow() - t1)

print('Creating fake keys (misses)...')
t1 = dt.utcnow()
misses = [str(uuid.uuid4()) for hit in hits]
print(dt.utcnow() - t1)

print('Timeing samples (hits)...')
t1 = dt.utcnow()
for key in hits:
    if key in mydict:
        value = values[mydict[key]]
    else:
        raise Exception('Could not find expected key: {key}'.format(key = key))
t2 = dt.utcnow() - t1
print(t2)
print('Retrival (hits): {cnt} k / sec'.format(cnt = int(len(hits)/t2.total_seconds()/1000)))

print('Timeing samples (misses)...')
t1 = dt.utcnow()
for key in misses:
    if key in mydict:
        raise Exception('Found unexpected key: {key}'.format(key = key))
t2 = dt.utcnow() - t1
print(t2)
print('Retrival (misses): {cnt} k / sec'.format(cnt = int(len(misses)/t2.total_seconds()/1000)))

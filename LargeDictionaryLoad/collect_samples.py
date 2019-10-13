# given a source file, take 5% as a random sample for performance testing
import pathlib
import random
from datetime import datetime as dt

### edit me - start
sample_size = .05
key_column = 1
source_file_name = 'd:/test/source_1.csv'
sample_file_name = 'd:/test/sample_1.csv'
### edit me - end

random.seed(0)
source_file_name = pathlib.Path(source_file_name)
sample_file_name = pathlib.Path(sample_file_name)

print('Reading source...')
t1 = dt.utcnow()
with open(source_file_name, 'r', encoding = 'utf-8', newline = '') as source_file:
    lines = source_file.readlines()
print(dt.utcnow() - t1)

print('Writing sample...')
t1 = dt.utcnow()
with open(sample_file_name, 'w', encoding = 'utf-8', newline = '') as sample_file:
    sample = random.sample(lines, int(len(lines) * sample_size))
    for line in sample:
        tokens = line.strip().split(',')
        key = tokens[key_column]
        sample_file.writelines(key + '\n')
print(dt.utcnow() - t1)

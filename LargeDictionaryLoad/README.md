# Large Dictionary Load

Simple tests on how to make a dictionary from a CSV.
Two tests were conducted: one data set had a fair bit of overlap in terms of prefixed keys, and the other was very unique in those terms.
The overall CSV files are ~5gb and the keys are english words.
The columns for key and value are known.
There is some level of concern as to access speed once the data structure is loaded, but the primary concern is initial load time and overall memory consumption.
Tests were run on an i7-6700K @ 4.00Ghz with 32Gb RAM running Win10 under Python 3.7.3 directly from `cmd.exe`.
The single run regeneration of everything is as follows:

```{shell}
python collect_samples.py
python test1.py
python test2.py
python test3.py
python test4.py
python test5.py
python test6.py
```

## Addtional Prerequsits

In addtion to the common prerequsits, others are needed.
This is because some of the imported packages need to be locally compiled and are not available as wheels.

* [Microsoft Visual C++ Build Tools 2015](https://visualstudio.microsoft.com/downloads)
* PIP packages
  * Notice that a [Fork](git+https://github.com/poke1024/DAWG.git@fix-cython-py3) is used

```{ps1}
choco install microsoft-visual-cpp-build-tools  -y
pip install -r requirements.txt
```

## Tests

* Line by line load into `mydict = {}`.
  [`test1.py`](./test1.py)
* Load as a generator into `mydict = dict()`.
  [`test2.py`](./test2.py)
* Read the full file then load.
  [`test3.py`](./test3.py)
* Use a [`DAWG`](https://github.com/pytries/DAWG).
  [`test4.py`](./test4.py)
* Use a [Trie](https://github.com/pytries/marisa-trie).
  [`test5.py`](./test5.py)
* Use a [BTree](https://github.com/zopefoundation/BTrees).
  [`test6.py`](./test6.py)
* `NumPy` load then process

## Results

[`test1.py`](./test1.py)

* Load time: 0:01:28.655617
* RAM: 19,736 MB
* Retrival (hits): 1177 k / sec
* Retrival (misses): 3861 k / sec

[`test2.py`](./test2.py)

* Load time: 0:01:23.504762
* RAM: 19,737 MB
* Retrival (hits): 1260 k / sec
* Retrival (misses): 4288 k / sec

[`test3.py`](./test3.py)

* Load time: 0:01:47.991263
* RAM: 19,744 MB
* Retrival (hits): 559 k / sec
* Retrival (misses): 3482 k / sec

[`test4.py`](./test4.py)

* Unable to build dictionary

[`test5.py`](./test5.py)

* Load time: 0:03:52.338609
* RAM: 8,399 MB
* Retrival (hits): 244 k / sec
* Retrival (misses): 3129 k / sec

[`test6.py`](./test6.py)

* Load time: 0:02:18.024301
* RAM: 18,689 MB
* Retrival (hits): 238 k / sec
* Retrival (misses): 1244 k / sec
# Large Dictionary Load

Simple tests on how to make a dictionary from a CSV.
The overall CSV file is ~5gb and the keys are english words.
The columns for key and value are known.
There is some level of concern as to access speed once the data structure is loaded, but the primary concern is initial load time and overall memory consumption.
Tests were run on an i7-6700K @ 4.00Ghz with 32Gb RAM running Win10 under Python 3.7.3 directly from `cmd.exe`.
Each test was run from a new `cmd.exe`

```{shell}
python collect_samples.py
python test1.py
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

* Line by line load into `mydict = {}`
  [`test1.py`](./text1.py)
* Line as a generator into `mydict = dict()`
  [`test2.py`](./text2.py)
* Read the full file then load
* use a [`DAWG`](https://github.com/pytries/DAWG)
* `NumPy` load then process

## Results

[`test1.py`](./text1.py)

* Load time: 0:01:28.655617
* RAM: 19,736 MB
* Retrival (hits): 1177 k / sec
* Retrival (misses): 3861 k / sec
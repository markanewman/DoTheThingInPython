# Large Dictionary Load

Simple tests on how to load a large dictionary into RAM.
The dictionary is ~5gb and the keys are english words. 

## Addtional Prerequsits

In addtion to the common prerequsits, others are needed

* [Microsoft Visual C++ Build Tools 2015](https://visualstudio.microsoft.com/downloads)
* PIP packages
  * Notice that a [Fork](git+https://github.com/poke1024/DAWG.git@fix-cython-py3) is used

```{ps1}
choco install microsoft-visual-cpp-build-tools  -y
pip install -r requirements.txt
```

## Tests

* Line by line load into a `x = {}`
* Read the full file then load
* use a [`DAWG`](https://github.com/pytries/DAWG)

## Results
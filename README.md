# Do The Thing (in Python!)

A collection of tests to help with performance considerations in other areas.
Each sub folder has a `README.md` to help understand the problem and is intended to be standalone.
You will probaly need to browse into the folder to tell what is going on.

# Prerequsits

The following packages need to be installed.
I recomend using [Chocolatey](https://chocolatey.org/install)

* [Python](https://www.python.org/downloads/windows/)

```{ps1}
if('Unrestricted' -ne (Get-ExecutionPolicy)) { Set-ExecutionPolicy Bypass -Scope Process -Force }
iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
refreshenv

choco install python3  -y
```
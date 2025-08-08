# popn-naming-type-cost

## Overview

- This script approximately calculates key-stroke counts which need to input certain music game-oriented names.
- Plus, enables us to compare whether it is more efficient to type title or genre to mention a particular song.
- [This article](https://signo.hatenablog.jp/entry/2023/01/01/234738) is based on the result.

## Requirements

- [pykakasi](https://codeberg.org/miurahr/pykakasi) (to parse Japanese phrase; requires **Python 3.7+**. The library advertises support for Python 3.6–3.9.)
- installing CSV file from [external pastebin](https://pastebin.com/TsMzbQi9)  
(Title and genre data might be KONAMI's Intellectual Property. In order to keep this repository as MIT License, *polluted* material would not be included.)

## Usage

ok, just run the code like this

``` bash
python3 main.py
```

## Features

- load name-packed CSV data
- parse Japanese phrase
- convert Japanese as Hepburn
- calculate typing-count
- export result as CSV file

## External Source

- [BEMANIWiki 2nd, pop'n music UniLab/旧曲リスト](https://bemaniwiki.com/index.php?pop%27n+music+UniLab/%B5%EC%B6%CA%A5%EA%A5%B9%A5%C8)

## Author

- [@signoiidx](https://twitter.com/signo_hacka)

## License

[MIT License](./license.txt)

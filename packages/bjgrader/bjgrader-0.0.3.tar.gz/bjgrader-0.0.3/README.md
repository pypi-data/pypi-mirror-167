# bjgrader

`bjgrader` 는 백준 알고리즘 사이트의 문제 별 sample input & output 을 바탕으로 손쉽게 채점해주는 라이브러리 입니다.

원하는 곳에서 `bjgrader`를 이용하여 파일을 생성 후, 알고리즘 풀이를 작성한 뒤, `bjgrader`로 채점하시면 됩니다.

`requests`와 `beautifulsoup4`를 바탕으로 sample input과 sample output을 가져와 채점하기에, 공개되지 않은 입력에 대해서는 채점하지 않습니다.

<br>

## Installation

```bash
pip install bjgrader
```

<br>

## Usage

### Create a solution file

```bash
python -m bjgrader -c file_name.py
```

<br>

### Grade the solution file

```bash
python -m bjgrader -n file_name.py
```
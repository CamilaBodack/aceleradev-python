# .travis.yml
config = """
language: python
python:
    - "2.7"
    - "3.7"
    - "7.1.1"
    - "7.1.1-beta0"
    - "pypy"
    - "pypy3"


install:
    - pip install -r requirements.txt

script: pytest

"""

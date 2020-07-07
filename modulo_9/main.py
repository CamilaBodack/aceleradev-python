# .travis.yml
config = """
language: python
python:
    - "2.7"
    - "3.7"
    - "pypy"
    - "pypy3"

stages:
    - name: test
    - name: deploy

install:
    - pip install -r requirements.txt

script: pytest

jobs:
    - stage: test
    - stage: deploy

"""

# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/TUW-GEO/eotransform-pandas/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                                                    |    Stmts |     Miss |   Branch |   BrPart |   Cover |   Missing |
|------------------------------------------------------------------------ | -------: | -------: | -------: | -------: | ------: | --------: |
| src/eotransform\_pandas/\_\_init\_\_.py                                 |        1 |        0 |        0 |        0 |    100% |           |
| src/eotransform\_pandas/\_version.py                                    |        1 |        0 |        0 |        0 |    100% |           |
| src/eotransform\_pandas/filesystem/\_\_init\_\_.py                      |        0 |        0 |        0 |        0 |    100% |           |
| src/eotransform\_pandas/filesystem/gather.py                            |       32 |        0 |       16 |        1 |     98% |    37->40 |
| src/eotransform\_pandas/filesystem/naming/\_\_init\_\_.py               |        0 |        0 |        0 |        0 |    100% |           |
| src/eotransform\_pandas/filesystem/naming/geopathfinder\_conventions.py |        8 |        0 |        0 |        0 |    100% |           |
| src/eotransform\_pandas/transformers/\_\_init\_\_.py                    |        0 |        0 |        0 |        0 |    100% |           |
| src/eotransform\_pandas/transformers/group\_by\_n.py                    |       21 |        0 |        2 |        0 |    100% |           |
|                                                               **TOTAL** |   **63** |    **0** |   **18** |    **1** | **99%** |           |


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://raw.githubusercontent.com/TUW-GEO/eotransform-pandas/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/TUW-GEO/eotransform-pandas/blob/python-coverage-comment-action-data/htmlcov/index.html)

This is the one to use if your repository is private or if you don't want to customize anything.

### [Shields.io](https://shields.io) Json Endpoint

[![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/TUW-GEO/eotransform-pandas/python-coverage-comment-action-data/endpoint.json)](https://htmlpreview.github.io/?https://github.com/TUW-GEO/eotransform-pandas/blob/python-coverage-comment-action-data/htmlcov/index.html)

Using this one will allow you to [customize](https://shields.io/endpoint) the look of your badge.
It won't work with private repositories. It won't be refreshed more than once per five minutes.

### [Shields.io](https://shields.io) Dynamic Badge

[![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2FTUW-GEO%2Feotransform-pandas%2Fpython-coverage-comment-action-data%2Fendpoint.json)](https://htmlpreview.github.io/?https://github.com/TUW-GEO/eotransform-pandas/blob/python-coverage-comment-action-data/htmlcov/index.html)

This one will always be the same color. It won't work for private repos. I'm not even sure why we included it.

## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.
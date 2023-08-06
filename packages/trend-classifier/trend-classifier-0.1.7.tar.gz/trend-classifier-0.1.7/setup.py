# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['trend_classifier']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.5.3,<4.0.0',
 'numpy>=1.23.2,<2.0.0',
 'pandas>=1.4.4,<2.0.0',
 'pydantic>=1.10.1,<2.0.0']

setup_kwargs = {
    'name': 'trend-classifier',
    'version': '0.1.7',
    'description': 'Package for automated signal segmentation, trend classification and analysis.',
    'long_description': '# Trend classifier\n![](https://img.shields.io/pypi/v/trend-classifier.svg)\n![](https://img.shields.io/pypi/pyversions/trend-classifier.svg)\n![](https://img.shields.io/pypi/l/trend-classifier.svg)\n![](https://img.shields.io/pypi/dm/trend-classifier.svg)\n[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/izikeros/trend_classifier/main.svg)](https://results.pre-commit.ci/latest/github/izikeros/trend_classifier/main)\n[![Black formatter](https://github.com/izikeros/trend_classifier/actions/workflows/black.yml/badge.svg)](https://github.com/izikeros/trend_classifier/actions/workflows/black.yml)\n[![flake8](https://github.com/izikeros/trend_classifier/actions/workflows/flake8.yml/badge.svg)](https://github.com/izikeros/trend_classifier/actions/workflows/flake8.yml)\n[![pytest](https://github.com/izikeros/trend_classifier/actions/workflows/pytest.yml/badge.svg)](https://github.com/izikeros/trend_classifier/actions/workflows/pytest.yml)\n[![Maintainability](https://api.codeclimate.com/v1/badges/081a20bb8a5201cd8faf/maintainability)](https://codeclimate.com/github/izikeros/trend_classifier/maintainability)\n[![Test Coverage](https://api.codeclimate.com/v1/badges/081a20bb8a5201cd8faf/test_coverage)](https://codeclimate.com/github/izikeros/trend_classifier/test_coverage)\n\nLibrary for automated signal segmentation, trend classification and analysis.\n\n## Installation\n\n1. The package is pip-installable. To install it, run:\n\n   ```sh\n   pip3 install trend-classifier\n   ```\n\n## Usage\n### Pandas DataFrame Input\nusage:\n```python\nimport yfinance as yf\nfrom trend_classifier import Segmenter\n\n# download data from yahoo finance\ndf = yf.download("AAPL", start="2018-09-15", end="2022-09-05", interval="1d", progress=False)\n\nx_in = list(range(0, len(df.index.tolist()), 1))\ny_in = df["Adj Close"].tolist()\n\nseg = Segmenter(x_in, y_in, n=20)\nseg.calculate_segments()\n```\n\nFor graphical output use `Segmenter.plot_segments()`:\n```python\nseg.plot_segments()\n```\n\n![Segmentation example](https://github.com/izikeros/trend_classifier/blob/main/img/screenshoot_1.jpg?raw=true)\n\nAfter calling method `Segmenter.calculate_segments()` segments are identified and information is stored in `Segmenter.segments` as list of Segment objects. Each Segment object. Each Segment object has attributes such as \'start\', \'stop\' - range of indices for the extracted segment, slope and many more attributes that might be helpful for further analysis.\n\nExemplary info on one segment:\n```python\nfrom devtools import debug\ndebug(seg.segments[3])\n```\nand you should see something like this:\n```\n    seg.segments[3]: Segment(\n        start=154,\n        stop=177,\n        slope=-0.37934038908585044,\n        offset=109.54630934894907,\n        slopes=[\n            -0.45173184100846725,\n            -0.22564684358754555,\n            0.15555037018051593,\n            0.34801127785130714,\n        ],\n        offsets=[\n            121.65628807526804,\n            83.56079272220015,\n            17.32660986821478,\n            -17.86417581658647,\n        ],\n        slopes_std=0.31334199799377654,\n        offsets_std=54.60900279722876,\n        std=0.933497081795997,\n        span=82.0,\n        reason_for_new_segment=\'offset\',\n    )\n```\nexport results to tabular format (pandas DataFrame):\n```python\nseg.segments.to_dataframe()\n```\n![](https://github.com/izikeros/trend_classifier/blob/main/img/to_dataframe.jpg?raw=true)\n(not all columns are shown)\n\n## License\n\n[MIT](LICENSE) © [Krystian Safjan](https://safjan.com/).\n',
    'author': 'Krystian Safjan',
    'author_email': 'ksafjan@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/izikeros/trend_classifier',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)

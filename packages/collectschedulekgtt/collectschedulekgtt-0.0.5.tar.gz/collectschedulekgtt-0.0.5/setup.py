# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['collectschedulekgtt']
setup_kwargs = {
    'name': 'collectschedulekgtt',
    'version': '0.0.5',
    'description': 'Модуль который использует Google таблицу КГТТ , для получения расписания',
    'long_description': '# ***Получение расписания с Google Таблицы КГТТ***\n____\n### Установка\n```\npip install collectschedulekgtt\n```\n### Импорт и инициализация\n```python\nfrom collectschedulekgtt import Collector\n\ncollector = Collector("Название группы")\n```\n### Пример\n\n```python\ncollector = Collector("1ИСИП-21-9")\ncollector.get_image()  # Вернет расписание для группы 1ИСИП-21-9\n```\n## Примечание\n>Важно чтобы таблица была открытой для общего доступа!\n## Полезные ссылки\n>[Страница на GitHub](https://github.com/DaniEruDai/collectschedulekgtt)\n> | [Страница на PyPi](https://pypi.org/project/collectschedulekgtt)\n\n\n',
    'author': 'DaniEruDai',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)

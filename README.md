# Pypograph

> Simple typographic tool for Python/Django.

## Usage

```python
from pypograph import Typograph
from pypograph import rules

typograph = Typograph([rules.QuoteRule, rules.DashRule])
typograph.typo('- Это "типограф"?') # -> '— Это «типограф»?'
```

## Usage with Django

Add `pypograph` to `INSTALLED_APPS` and try:

```html
{% load pypograph %}

{% typo %}
  <p>- Это "типограф"?</p>
{% endtypo %}

{% content|typo %}
```

You can configure rules by adding `TYPOGRAPH_RULES` into your `setting.py`:

```python
TYPOGRAPH_RULES = [
    'pypograph.rules.DashRule',
    ('pypograph.rules.QuoteRule', {'quotes': '“”'}),
]
```

## Сustom rules

```python
from pypograph.rules import BaseRule
from pypograph import Typograph


class MyOwnRule(BaseRule):
    config = {
      'from': 'a',
      'to': 'b',
    }

    def process(self, text):
        return text.replace(self.config['from'], self.config['to'])


typograph = Typograph([MyOwnRule])
typograph.typo('abc') # -> 'bbc'
```


## Testing

```sh
$ python -m unittest pypograph.tests
```

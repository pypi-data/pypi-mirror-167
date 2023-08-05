# django-markdownify-filter
A template filter to convert HTML strings to Markdown using [Markdownify](https://github.com/matthewwithanm/python-markdownify).

## Quick start
1. Add "markdownify_filter" to your INSTALLED_APPS setting like this:

```python
    INSTALLED_APPS = [
        ...
        'markdownify_filter',
    ]
```
2. Load the filter in the template using `{% load markdownify_filter %}`.

3. Us it on a HTML string like so: `{{ HTML.string | markdownify }}`
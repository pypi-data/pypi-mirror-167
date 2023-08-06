#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    {%- for option in options %}
    {%- if option[2] == "str" %}
    {{option[0]}}="{{option[1]}}",
    {%- else %}
    {{option[0]}}={{option[1]}},
    {%- endif %}
    {%- endfor %}
    packages=find_packages(),
    package_data={
    {%- for data in extra_options[0] %}
        "{{data[0]}}": [{{data[1]}}],
    {%- endfor %}
    },
    entry_points={
        "console_scripts": [
    {%- for script in extra_options[1] %}
            "{{script}}"
    {%- endfor %}
        ]
    }
)

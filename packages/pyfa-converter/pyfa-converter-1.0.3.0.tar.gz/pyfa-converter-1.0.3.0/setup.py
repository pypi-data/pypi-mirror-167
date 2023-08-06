# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyfa_converter', 'pyfa_converter.utils']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.65', 'pydantic>=1.6', 'python-multipart>=0.0.5,<0.0.6']

setup_kwargs = {
    'name': 'pyfa-converter',
    'version': '1.0.3.0',
    'description': 'Pydantic to fastapi model converter.',
    'long_description': '# pyfa-converter\nAllows you to convert pydantic models for fastapi param models - query, form, header, cookie, body, etc.\n\n\n\n### How to install?\n`pip install pyfa_converter`\n\n### How to simplify your life?\n```python3\nfrom datetime import datetime\nfrom typing import Optional\n\nfrom fastapi import FastAPI, UploadFile, File, Form\nfrom pydantic import BaseModel, Field\n\nfrom pyfa_converter import FormDepends, PyFaDepends\n\napp = FastAPI()\n\n\nclass PostContractBodySchema(BaseModel):\n    title: str = Field(..., description="Description title")\n    date: Optional[datetime] = Field(\n        None, description="Example: 2021-12-14T09:56:31.056Z"\n    )\n\n\n@app.post("/form-data-body")\nasync def example_foo_body_handler(\n    data: PostContractBodySchema = FormDepends(PostContractBodySchema),\n    # data1: PostContractBodySchema = PyFaDepends( # OR\n    #         model= PostContractBodySchema, _type=Form\n    #     ),\n    document: UploadFile = File(...),\n):\n    return {"title": data.title, "date": data.date, "file_name": document.filename}\n```\n\n---\n\n### What do I need to do?\n```python3\nfrom pyfa_converter import PyFaDepends, FormDepends, QueryDepends\nfrom fastapi import Header, Form\n...\n\nasync def foo(data: MyCustomModel = PyFaDepends(MyCustomModel, _type=Header)): ...\nasync def foo(data: MyCustomModel = PyFaDepends(MyCustomModel, _type=Form)): ...\n\nasync def foo(data: MyCustomModel = FormDepends(MyCustomModel)): ...\nasync def foo(data: MyCustomModel = QueryDepends(MyCustomModel)): ...\n```\n\n---\n\nIf you want to accept a file on an endpoint, then the content-type for that endpoint changes from application/json to www-form-data.\n\nFastAPI does not know how to override the pydantic schema so that parameters are passed as form.\nEven if you do\n\n`foo: CustomPydanticModel = Depends()`\nall model attributes will be passed as query, but we want them to become body, that\'s what this library exists for.\n\n### Usually you use something along the lines of:\n![image](https://user-images.githubusercontent.com/64792903/161484700-642e3d0e-242f-49f6-82e8-45c5e912a2c2.png)\n\nBut, if we accept a lot of fields, then the function becomes very large (the number of attributes for the endpoint increases and it does not look very good).\n\nThanks to this library, it is possible to force the conversion of Field fields into fields of FastAPI Form with full preservation of all attributes (alias, gt, te, description, title, example and more...)\n\n\n',
    'author': 'dotX12',
    'author_email': 'dev@shitposting.team',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/dotX12/pyfa-converter',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)

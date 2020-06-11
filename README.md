# MIME Type Description

Human readable MIME type descriptions based on [shared-mime-info](https://www.freedesktop.org/wiki/Software/shared-mime-info/).

## Install

```bash
pip install mimetype-description
```

## Usage

```python
from mimetypes import guess_type

from mimetype_description import get_mime_type_description

mime_type = guess_type('file.txt')[0]
description = get_mime_type_description(mime_type)
print(description)  # plain text document
```

## Test

```bash
pytest
```

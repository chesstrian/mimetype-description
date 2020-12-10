try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources
import xml.etree.ElementTree


class MimeTypeDescription:
    _mime_types = dict()
    _descriptions = dict()

    def __init__(self):
        lang_attr = '{http://www.w3.org/XML/1998/namespace}lang'
        shared_mime_info = '{http://www.freedesktop.org/standards/shared-mime-info}'
        data = pkg_resources.read_text(__package__, 'freedesktop.org.xml')
        root = xml.etree.ElementTree.fromstring(data)

        for mime_type in root:
            _type = mime_type.attrib['type']
            self._descriptions[_type] = dict()

            for child in mime_type:
                _tag = child.tag.replace(shared_mime_info, '')
                if _tag == 'comment':
                    lang = child.attrib[lang_attr] if child.attrib else 'en'
                    self._descriptions[_type][lang] = child.text
                elif _tag == 'glob':
                    ext = child.attrib['pattern'].replace('*.', '')
                    self._mime_types[ext] = _type

    def get_description(self, mime_type: str, language: str) -> (str, None):
        try:
            return self._descriptions[mime_type][language]
        except KeyError:
            return None

    def get_mime_type(self, filename: str) -> (str, None):
        try:
            return self._mime_types.get(filename.split('.')[-1])
        except IndexError:
            return None


_instance = MimeTypeDescription()


def get_mime_type_description(mime_type: str, language: str = 'en') -> str:
    return _instance.get_description(mime_type, language)


def guess_mime_type(filename: str) -> str:
    return _instance.get_mime_type(filename)


__all__ = ('get_mime_type_description', 'guess_mime_type')

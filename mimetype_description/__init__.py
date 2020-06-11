import importlib.resources as pkg_resources
import xml.etree.ElementTree

from cached_property import cached_property


class UnsupportedMimeType(Exception):
    pass


class UnsupportedLanguage(Exception):
    pass


class MimeTypeDescription:

    @cached_property
    def _descriptions(self) -> dict:
        result = dict()
        lang_attr = '{http://www.w3.org/XML/1998/namespace}lang'
        shared_mime_info = '{http://www.freedesktop.org/standards/shared-mime-info}'
        data = pkg_resources.read_text(__package__, 'freedesktop.org.xml')
        root = xml.etree.ElementTree.fromstring(data)

        for mime_type in root:
            _type = mime_type.attrib['type']
            result[_type] = dict()

            for child in mime_type:
                _tag = child.tag.replace(shared_mime_info, '')
                if _tag == 'comment':
                    lang = child.attrib[lang_attr] if child.attrib else 'en'
                    result[_type][lang] = child.text

        return result

    def get_description(self, mime_type: str, language: str) -> str:
        try:
            return self._descriptions[mime_type][language]
        except KeyError as e:
            if f"'{mime_type}'" in e.__str__():
                raise UnsupportedMimeType(f"Unsupported MIME type: '{mime_type}'")
            elif f"'{language}'" in e.__str__():
                raise UnsupportedLanguage(f"Unsupported language: '{language}'")


_instance = MimeTypeDescription()


def get_mime_type_description(mime_type: str, language: str = 'en') -> str:
    return _instance.get_description(mime_type, language)


__all__ = ('get_mime_type_description', 'UnsupportedMimeType', 'UnsupportedLanguage')

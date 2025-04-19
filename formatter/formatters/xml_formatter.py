import lxml.etree
from formatter.formatters.base_formatter import BaseFormatter
from formatter.registry import register_formatter
import lxml

@register_formatter("xml")
class XmlFormatter(BaseFormatter):
    def _serialize(self, content, indent = 4, separators=...):
        return lxml.etree.tostring(content, pretty_print=True, encoding="unicode")

    def _deserialize(self, file):
        parser = lxml.etree.XMLParser(remove_blank_text=True)
        tree = lxml.etree.parse(file, parser)
        return tree

    def get_format_name(self):
        return "XML"

    def get_format_extension(self):
        return ".xml"





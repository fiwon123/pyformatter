from formatter.formatters.base_formatter import BaseFormatter
from formatter.registry import register_formatter
from lxml import etree

@register_formatter("xml")
class XmlFormatter(BaseFormatter):
    def _serialize(self, content, indent = 4, separators=...):
        return etree.tostring(content, pretty_print=True, encoding="unicode")

    def _deserialize(self, file):
        parser = etree.XMLParser(remove_blank_text=True)
        tree = etree.parse(file, parser)
        return tree

    def get_format_name(self):
        return "XML"

    def get_format_extension(self):
        return ".xml"





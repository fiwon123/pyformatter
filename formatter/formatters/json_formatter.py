from formatter.formatters.base_formatter import BaseFormatter
from formatter.registry import register_formatter
import json

@register_formatter("json")
class JsonFormatter(BaseFormatter):
    def _serialize(self, content, indent = 4, separators=...):
        return json.dumps(content, indent = indent, separators= separators)

    def _deserialize(self, file):
        return json.load(file)

    def get_format_name(self):
        return "JSON"

    def get_format_extension(self):
        return ".json"




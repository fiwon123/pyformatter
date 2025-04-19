from formatter.formatters.base_formatter import BaseFormatter
from formatter.registry import register_formatter
from tomli_w import dumps
import toml

@register_formatter("toml")
class TomlFormatter(BaseFormatter):
    def _serialize(self, content, indent = 4, separators=...):
        return dumps(content)

    def _deserialize(self, file):
        return toml.load(file)

    def get_format_name(self):
        return "TOML"

    def get_format_extension(self):
        return ".toml"





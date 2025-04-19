from formatter.formatters.base_formatter import BaseFormatter
from formatter.registry import register_formatter
import yaml


@register_formatter("yaml")
class YamlFormatter(BaseFormatter):
    def _serialize(self, content, indent = 4, separators=...):
        return yaml.safe_dump(content, indent = indent)

    def _deserialize(self, file):
        return yaml.safe_load(file)

    def get_format_name(self):
        return "YAML"

    def get_format_extension(self):
        return ".yaml"





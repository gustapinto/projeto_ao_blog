from pathlib import Path

from markdown import Markdown

from blog.settings import PROJECT_ROOT


class MarkdownParser:
    def __init__(self):
        self.resource_files_path = PROJECT_ROOT / 'resources/markdown'

        markdown_files_path = Path(self.resource_files_path).rglob('*.md')

        self.markdown_files_path_list = list(markdown_files_path)

        self.markdown_object = Markdown(extensions=['meta'])

    def get_html_strings_list_with_metadata(self):
        if self.markdown_files_path_list:
            html_strings_and_metadata_map = map(self._parse_md_file_to_html_string_with_metadata,
                                                self.markdown_files_path_list)

            html_strings_and_metadata_list = list(html_strings_and_metadata_map)

            return html_strings_and_metadata_list

        return None

    def _parse_md_file_to_html_string_with_metadata(self, file_path):
        with open(file_path, 'r') as markdown_file:
            markdown_string = markdown_file.read()

            html_string = self.markdown_object.convert(markdown_string)
            html_metadata = self.markdown_object.Meta

            html_string_metadata_dict = {
                'html': html_string,
                'metadata': html_metadata,
            }

            self.markdown_object.reset()

        return html_string_metadata_dict

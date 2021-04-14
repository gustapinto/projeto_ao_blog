from django.shortcuts import render

from blog.core.utils.parsers.markdown import MarkdownParser

def index(request):
    markdown_parser = MarkdownParser()

    context = {'posts': markdown_parser.get_html_strings_list_with_metadata()}

    return render(request, 'core/list.html', context)

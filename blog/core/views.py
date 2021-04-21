from django.shortcuts import render, redirect

from blog.core.utils.parsers.markdown import MarkdownParser


def redirect_url(request):
    url = request.META['RAW_URI']

    redirect_to_relation = {
        '/': '/posts/',
    }

    return redirect(redirect_to_relation[url])

def list_posts(request):
    markdown_parser = MarkdownParser()

    posts_html_metadata_list = markdown_parser.get_html_strings_list_with_metadata()

    context = {'posts': posts_html_metadata_list}

    return render(request, 'core/posts/list.html', context)

def view_post(request, filename):
    markdown_parser = MarkdownParser()

    post_html_metadata = markdown_parser.get_html_strings_list_with_metadata(filename)

    context = {'post': post_html_metadata[0]}

    return render(request, 'core/posts/view.html', context)

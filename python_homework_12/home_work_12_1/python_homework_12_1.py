import typing


def delete_html_tags(html_file: typing.Any, result_file: typing.Any = 'cleaned.txt') -> None:
    """
    Function take text in 'draft.html' delete our html-tags
    and save rezult in file 'cleaned.txt'
    :param html_file: str in 'draft.html'
    :param result_file: str in 'cleaned.txt'
    """
    with open(html_file, 'r', encoding='utf-8') as file:
        html = file.read()
        while html.count("<"):
            html = html.replace(html[html.find("<"):html.find(">") + 1], "")
        html = '\n'.join(line.strip() for line in html.split('\n') if line.strip())
    with open(result_file, 'w', encoding='utf-8') as result_file:
        result_file.write(html)


delete_html_tags('draft.html')

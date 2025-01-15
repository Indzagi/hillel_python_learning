import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    """
    Function take text in 'draft.html' delete our html-tags
    and save rezult in file 'cleaned.txt'
    :param html_file: str in 'draft.html'
    :param result_file: str in 'cleaned.txt'
    """
    with open(html_file, 'r', encoding='utf-8') as file:
        html = file.read()
        html = re.sub(r'<[^>]+>', '', html)
        html = '\n'.join(i.strip() for i in html.split('\n') if i.strip())
    with open(result_file, 'w', encoding='utf-8') as result_file:
        result_file.write(html)


delete_html_tags('../home_work_12_1/draft.html')

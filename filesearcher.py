import os
import collections

SearchResult = collections.namedtuple('SearchResult',
                                      'file, line, text')


def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print('Sorry, location not available')
        return

    text = get_search_text_from_user()
    if not text:
        print('Text not available')

    matches = search_folder(folder, text)
    match_count = 0

    for m in matches:
        match_count += 1
        # print('------------MATCH------------')
        # print('file: ' + m.file)
        # print('line: {}'.format(m.line))
        # print('match: ' + m.text.strip())
        # print()

    print('Found {:,} matches'.format(match_count))


def print_header():
    print('-----------------------------------------')
    print('             FILE SEARCHER')
    print('-----------------------------------------')


def get_folder_from_user():
    folder = input("What folder do you want to search? ")
    if not folder or not folder.strip():
        return None
    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input('What are you looking for? [single phrases only]: ')
    return text.lower()


def search_folder(folder, text):
    # print('Would search {} for {}'.format(folder, text))

    all_matches = []
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            yield from search_folder(full_item, text)
            # matches = search_folder(full_item, text)
        else:
            yield from search_file(full_item, text)
            # matches = search_file(full_item, text)
        # all_matches.extend(matches)

    # return all_matches


def search_file(file_name, search_text):
    try:
        with open(file_name, 'r', encoding='utf-8') as fin:
            matches = []
            line_count = 0
            for line in fin:
                line_count += 1
                if line.lower().find(search_text) >= 0:
                    m = SearchResult(file=file_name, line=line_count, text=line)
                    matches.append(m)
            return matches
    except:
        return []


if __name__ == '__main__':
    main()

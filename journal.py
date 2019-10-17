import os


def load(name):

    """
    This method creates and loads a new journal

    :param name: The base name of the journal to load
    :return: A new journal data structure populated with the file
    """
    data = []
    file_name = get_full_path(name)
    print('...... loading from: {}'.format(file_name))

    if os.path.exists(file_name):
        with open(file_name) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(name, data):
    file_name = get_full_path(name)
    print('...... saving to: {}'.format(file_name))

    with open(file_name, 'w') as fout:
        for entry in data:
            fout.write(entry + '\n')


def get_full_path(name):
    file_name = os.path.abspath(os.path.join('.', 'Journals', name + '.jrl'))
    return file_name


def add_entry(data, text):
    data.append(text)

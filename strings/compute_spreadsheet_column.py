ASCII_INDEX = 65
NUM_ALPHABETS = 26


def compute_spreadsheet_column(column_index):
    encoding = []
    while column_index > 0:
        rem = (column_index - 1) % NUM_ALPHABETS
        encoding.append(chr(ASCII_INDEX + rem))
        column_index = (column_index - 1) // NUM_ALPHABETS
    return ''.join(encoding[::-1])


def compute_spreadsheet_column_0_index(column_index):
    return compute_spreadsheet_column(column_index + 1)


def compute_column_from_column_name(column_name):
    column_index = 0
    for ind, char in enumerate(column_name[::-1]):
        val = ord(char) - ASCII_INDEX + 1
        column_index += val * (NUM_ALPHABETS ** ind)
    return column_index


def main():
    assert compute_spreadsheet_column(1) == 'A'
    assert compute_spreadsheet_column(2) == 'B'
    assert compute_spreadsheet_column(27) == 'AA'
    assert compute_spreadsheet_column(63) == 'BK'
    assert compute_spreadsheet_column(702) == 'ZZ'
    assert compute_column_from_column_name('A') == 1
    assert compute_column_from_column_name('Z') == 26
    assert compute_column_from_column_name('B') == 2
    assert compute_column_from_column_name('AA') == 27
    assert compute_column_from_column_name('AB') == 28
    assert compute_column_from_column_name('BK') == 63
    assert compute_column_from_column_name('ZZ') == 702


if __name__ == "__main__":
    main()

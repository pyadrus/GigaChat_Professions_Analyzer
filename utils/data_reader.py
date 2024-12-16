import openpyxl as op


def open_list_gup(filepath):
    """
    Читает данные из Excel-файла и возвращает список участков и профессий.

    :param filepath: Путь к Excel-файлу.
    :return: Список списков с данными [участок, профессия].
    """
    wb = op.load_workbook(filepath)
    ws = wb.active
    list_gup = []

    for row in ws.iter_rows(min_row=1, max_row=69, min_col=1, max_col=2):
        list_gup.append([cell.value for cell in row])

    return list_gup

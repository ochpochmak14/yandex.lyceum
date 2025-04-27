import xlsxwriter


def export_check(text):
    workbook = xlsxwriter.Workbook("res.xlsx")
    worksheet = workbook.add_worksheet()

    text = text.strip().split("\n")

    for i in range(len(text)):
        item, price, quantity = text[i].split("\t")
        worksheet.write(i, 0, item)
        worksheet.write(i, 1, float(price))
        worksheet.write(i, 2, int(quantity))
        worksheet.write_formula(i, 3, f"=B{i + 1}*C{i + 1}")

    worksheet.write(len(text), 0, "Итого")
    worksheet.write_formula(len(text), 3, f"=SUM(D1:D{len(text)})")

    workbook.close()

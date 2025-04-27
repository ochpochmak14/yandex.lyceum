import xlsxwriter

workbook = xlsxwriter.Workbook("res.xlsx")
worksheet = workbook.add_worksheet()

data = [
    ("Питание", 1200),
    ("Развлечения", 1500),
    ("Учеба", 300),
    ("Лечение", 100),
    ("Прочее", 670),
]

for row, (item, price) in enumerate(data):
    worksheet.write(row, 0, item)
    worksheet.write(row, 1, price)

chart = workbook.add_chart({"type": "pie"})

chart.add_series(
    {
        "name": "Распределение расходов",
        "categories": "=Sheet1!A1:A5",
        "values": "=Sheet1!B1:B5",
    }
)

worksheet.insert_chart("C3", chart)

workbook.close()

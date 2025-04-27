import xlsxwriter


def export_check(text):
    workbook = xlsxwriter.Workbook("res.xlsx")

    receipts = list(map(lambda x: sorted(x.split("\n")), text.split("---")))
    for receipt in receipts:
        grouped_items = {}
        for line in receipt:
            if line == "":
                continue

            parts = line.split("\t")
            item, price = parts[0], int(parts[1])
            quantity = int(parts[2])

            key = (item, price)
            if key in grouped_items:
                grouped_items[key] += quantity
            else:
                grouped_items[key] = quantity

        item_list = list(grouped_items.keys())
        formatted_items = []
        for entry in item_list:
            formatted_items.append([entry[0], int(grouped_items[entry]), int(entry[1])])
        formatted_items.sort()

        ordered_items = {}
        for entry in formatted_items:
            ordered_items[(entry[0], entry[2])] = grouped_items[(entry[0], entry[2])]
            del grouped_items[(entry[0], entry[2])]

        if ordered_items:
            worksheet = workbook.add_worksheet()
            for row, (item_price, quantity) in enumerate(ordered_items.items()):
                worksheet.write(row, 0, item_price[0])
                worksheet.write(row, 1, float(item_price[1]))
                worksheet.write(row, 2, float(quantity))
                worksheet.write(row, 3, f"=B{row + 1}*C{row + 1}")

            row += 1

            worksheet.write(row, 0, "Итого")
            worksheet.write(row, 3, f"=SUM(D1:D{row})")

    workbook.close()

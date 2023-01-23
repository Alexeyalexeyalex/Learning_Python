def ExportValues(value):
    with open('DATA.txt', 'a',encoding='utf-8') as file:
        for i in value:
            file.write(f"{i} ")
        file.write("\n")
        print("Данные внесены")
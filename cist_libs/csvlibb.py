import csv

def open_and_read(filename : str, date_now : str) -> str:
    no_classes = True
    classes_str = f"<u><b>Classes at {date_now}</b></u>\n\n"
    try:
        print(f"Opening file -> {filename}")
        with open(f"csvFiles\\{filename}", newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=",")
            for row in reader:
                if row['Дата начала'] == date_now:
                    no_classes = False
                    classes_str += f"{row['Время начала'][:-3]} - {row['Время завершения'][:-3]} \n{row['Тема']}\n\n"
    except Exception as e:
        print(f"Orrupted error while opening file ({filename}): {e}")
    if no_classes == True:
        return "<u><b>No classes today!</b></u>"
    else:
        return classes_str

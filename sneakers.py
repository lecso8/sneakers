import pprint


def load_data(filename):
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()

    header = lines[0].strip().split(",")
    data = []
    for line in lines[1:]:
        values = line.strip().split(",")
        shoe = {header[i]: values[i] for i in range(len(header))}
        data.append(shoe)

    return data


def choose(data):
    options = {
        "1": "title",
        "2": "color",
        "3": "full_price",
        "4": "current_price",
        "5": "publish_date"
    }

    print("Döntsd el, melyik szempont alapján legyenek a cipők rendszerezve!")
    for key, value in options.items():
        print(f"{key} - {value}")

    choice = input("Add meg az adott lehetőség számát! ")
    key = options.get(choice)

    if key:
        return sorted(data, key=lambda x: x[key])
    else:
        print("Hiba.")
        return data


def main():
    filename = "sneakers.csv"
    data = load_data(filename)
    sorted_data = choose(data)

    pprint.pprint(sorted_data)


main()

def display_message(message: list[dict]) -> None:

    for entry in sorted(message, key=lambda k: k['code']):
        print(entry["data"], end="")


def create_dict(raw: str) -> list[dict[int:str]]:

    obj: list[dict[int:str]] = []

    for text in raw.split("|"):
        obj.append({"code": int(text[1:3]), "data": text[5:-2]})

    return obj


def build_raw_text(raw: str) -> tuple[str, int]:

    append: int = 1

    data: str = ""

    for chr in list(raw):

        data += chr

        if chr == "]":
            data += "|"
            append = 0
            break

    return data, append


def read_file(path_file: str) -> None:

    append: int = 0

    raw_text: str = ""

    with open(path_file, 'r') as f:

        while raw_data := f.read(15):  # read 15 byte at a time

            index = raw_data.find("[")

            if index > -1 or append > 0:

                text, append = build_raw_text(raw_data[index:]
                                              if index > -1 else raw_data)
                raw_text += text

    if raw_text:
        display_message(create_dict(raw_text[:-1]))


def main() -> None:

    try:
        path_file: str = "./texto.dat"

        read_file(path_file)

    except Exception as e:

        print(e)


main()

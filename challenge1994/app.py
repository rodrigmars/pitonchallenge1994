
def read_message(path_file, total_bytes):

    def convert_to_raw_list(raw: str) -> list[dict[int:str]]:

        raw_list: list[dict[int:str]] = []

        for text in raw.split("|"):
            raw_list.append({"index": text[1:3], "raw-text": text[5:-2]})

        return raw_list

    def display_message(raw_list: list[dict]) -> None:

        for entry in sorted(raw_list, key=lambda k: k['index']):
            print(entry["raw-text"], end="")

    def build_raw_text(raw: str) -> tuple[str, int]:

        append: int = 1

        raw_text: str = ""

        for chr in list(raw):

            raw_text += chr

            if chr == "]":
                raw_text += "|"
                append = 0
                break

        return raw_text, append

    def get_raw_text(path_file: str, total_bytes: int) -> str:

        append: int = 0

        raw_text: str = ""

        with open(path_file, 'r') as f:

            while raw_data := f.read(total_bytes):

                index = raw_data.find("[")

                if index > -1 or append > 0:

                    text, append = build_raw_text(raw_data[index:]
                                                  if index > -1 else raw_data)
                    raw_text += text

        return raw_text[:-1]

    return display_message(convert_to_raw_list(get_raw_text(path_file, total_bytes)))


def main() -> None:

    try:
        path_file: str = "./texto.dat"

        total_bytes: int = 15

        read_message(path_file, total_bytes)

    except Exception as e:

        print(e)


main()

def read_file(path_file:str) -> None:
    
    LEFT_BRACKET:str = "["

    RIGHT_BRACKET:str = "]"

    text:str = "" 

    with open(path_file, 'r') as f:
        
        while text := f.read(15):  # read 15 byte at a time

            if text.find(LEFT_BRACKET) > -1:
                print("start")

            if text.find(RIGHT_BRACKET) > -1:
                print("end")
            
            if not text:  # check for EOF
                print("chegou aqui")
                break
            # process the byte (e.g., print its ASCII value)
            print(">>>", text)

def main() -> None:

    try:
       path_file:str = "./texto.dat"

       read_file(path_file)

    
    except Exception as e:

        print(e)

    ...

main()


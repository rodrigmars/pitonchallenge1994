def read_file(path_file:str)->None:
    
    with open(path_file, 'r') as f:
        
        while byte := f.read(15):  # read 15 byte at a time
        
            if not byte:  # check for EOF
                print("chegou aqui")
                break
            # process the byte (e.g., print its ASCII value)
            print(">>>", byte)

def main() -> None:

    try:
       path_file:str = "./texto.dat"

       read_file(path_file)

    
    except Exception as e:

        print(e)

    ...

main()


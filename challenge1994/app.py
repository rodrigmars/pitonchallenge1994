def read_file(path_file:str) -> None:
    
    LEFT_BRACKET:str = "["

    RIGHT_BRACKET:str = "]"

    text:str = "" 

    def build_frase(raw:str):
        
        data:str = ""
        
        for chr in raw.split(): 
            
            data += chr
            
            if chr == "]":
                break;
                
        return data    

    with open(path_file, 'r') as f:
        
        while raw_data := f.read(15):  # read 15 byte at a time

            if raw_data.find(LEFT_BRACKET) > -1:
                raw_data += build_frase(raw_data) 
       
            if not raw_data:  # check for EOF
                print("chegou aqui")
                break
            # process the byte (e.g., print its ASCII value)
            print(">>>", raw_data)

def main() -> None:

    try:
       path_file:str = "./texto.dat"

       read_file(path_file)

    
    except Exception as e:

        print(e)

    ...

main()


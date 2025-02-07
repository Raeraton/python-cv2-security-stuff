



def get_log_to_send() -> bytes:
    outp:bytes
    with open("log.txt", "rb") as file:
        outp = file.read()
        file.close()
    
    return outp
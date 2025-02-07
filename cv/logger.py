from datetime import datetime


class My_logger:
    
    def __init__(self):
        self.file = open( "log.txt", "at" )

    def close(self):
        self.file.close()

    def add_log(self, text):
        now = datetime.now()

        self.file.write(
            f"{now.year}\t{now.month}\t{now.day}\t{now.hour}\t{now.minute}\t{now.second}\t{text}\n"
        )
        self.file.close()
        self.file = open( "log.txt", "at" )



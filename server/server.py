from http.server import BaseHTTPRequestHandler, HTTPServer

import server.data_packer as data_packer



hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if "/" == self.path:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            with open( "server/page/index.html", "rb" ) as file:
                self.wfile.write( file.read() )
                file.close()
        
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            with open( "server/page"+self.path, "rb" ) as file:
                self.wfile.write( file.read() )
                file.close()
    



    def do_POST(self):
        self.send_response(200)
        self.end_headers()

        cont_size = int( self.headers.get("Content-Length") )
        request = self.rfile.read(cont_size)
        data = b'SzB'
        if request == b'LOG':
            data = data_packer.get_log_to_send()


        self.wfile.write(data)
        return



def start_server():      
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
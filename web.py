from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html lang="en">
<head>
<h1>Welcome All This is My WebServer...</h1>
<h2>This is KARTHIKEYAN D from AI&DS Dept</h2>
</head>
<button>
    Click Me!!
</button>
<br>
<br><br>
<style>
    h2{
        color: darkblue;
    }
    button{
        background-color: red;
        color: white;
        border-radius: 2px;
        cursor: pointer;
    }


</style>
<body>
    <table border="1" cellpadding="7" cellspacing="6">
        <tr>
            <th>S No</th>
            <th>NAME</th>
            <th>DEPT</th>
            <th>REG NO</th>
        </tr>
        <tr>
            <td>1</td>
            <td>KARTHIKEYAN D</td>
            <td>AI&DS</td>
            <td>212224230115</td>
        </tr>
        <tr>
            <td>2</td>
            <td>KISHORE M</td>
            <td>CSE</td>
            <td>212224040161</td>
        </tr>
        
    </table>
    
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',80)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
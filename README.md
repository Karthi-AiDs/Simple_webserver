# EX01 Developing a Simple Webserver
## Date: 09/03/2025

## AIM:
To develop a simple webserver to serve html pages and display the list of students Name ,Regno and Department.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
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
```


## OUTPUT:

![alt text](<Screenshot (37).png>)
![alt text](<Screenshot (38).png>)


## RESULT:
The program for implementing simple webserver is executed successfully.


from datetime import datetime
dayofweek = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
monthStr = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def default_fobidden404(dt : datetime = datetime.now()) -> str:
    import sys
    d = dt.day
    m = dt.month
    y = dt.year
    return f'HTTP/1.1 404 Not Found\r\nDate:{dayofweek[(d + 2*m + (3 * (m + 1)) // 5 + y + (y//4)) % 7]}'\
f' {monthStr[dt.month]} {dt.year} at {dt.hour}:{dt.minute}:{dt.second} GMT\r\nServer: FullstackMQTT/0.0.1 ({sys.platform})'\
f'\n\rcontent-type:text/html\r\n\r\n'\
            """
            \r<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fullstack MQTT Server v0.0.1</title>
    <style>
        body{
            background-color: bisque;
        }
        .title{
            font-size: larger;
            color: #e31;
        }
        .content{
            font-size: 1.25rem;
            color: #11f;
        }
        .decuss{
            font-size: 1.1rem;
            color: #444;
            position: absolute;
            bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="title">
        <h1>Fobidden 404</h1>
    </div>
    <div class="content">
        <span>We can't found any link same you need in my category</span>
    </div>
    <div class="decuss">
        <span>@fullstackmqtt/0.0.1</span>
    </div>
</body>
</html>"""
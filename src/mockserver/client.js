var mockServerClient = require('mockserver-client').mockServerClient;
mockServerClient("localhost", 1080).mockAnyResponse({
    "httpRequest": {
        "method": "POST",
        "path": "/login",
        "body": '{"username": "foo", "password": "bar"}'
    },
    "httpResponse": {
        "statusCode": 302,
        "headers": {
            "Location" : [ "https://www.mock-server.com" ]
        },
        "cookies": {
            "sessionId" : "2By8LOhBmaW5nZXJwcmludCIlMDAzMW"
        }
    }
});

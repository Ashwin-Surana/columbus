from unittest import TestCase

from columbus.parser import AWSHttpParser


class TestHttpParser(TestCase):

    def test_aws_parser(self):
        event = {
            "resource": "/ping",
            "path": "/ping",
            "httpMethod": "POST",
            "headers": {
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "CloudFront-Forwarded-Proto": "https",
                "CloudFront-Is-Desktop-Viewer": "true",
                "CloudFront-Is-Mobile-Viewer": "false",
                "CloudFront-Is-SmartTV-Viewer": "false",
                "CloudFront-Is-Tablet-Viewer": "false",
                "CloudFront-Viewer-Country": "IN",
                "Content-Type": "multipart/form-data; boundary=--------------------------503769280530400724074437",
                "Host": "uap6yawi5d.execute-api.us-east-1.amazonaws.com",
                "Postman-Token": "461d11fd-df49-4572-8ab4-bd75d155577f",
                "User-Agent": "PostmanRuntime/7.26.5",
                "Via": "1.1 1e1845653f1116e06ee8f549030eac08.cloudfront.net (CloudFront)",
                "X-Amz-Cf-Id": "fRjOWCVKr7IaONi9X4U8-THOc3OElkUgHPmJOpdifXwMrTHKVBT6Eg==",
                "X-Amzn-Trace-Id": "Root=1-5fb7524d-606921ef41ca358e6768fc2a",
                "X-Forwarded-For": "157.49.217.6, 52.46.49.166",
                "X-Forwarded-Port": "443",
                "X-Forwarded-Proto": "https"
            },
            "multiValueHeaders": {
                "Accept": [
                    "*/*"
                ],
                "Accept-Encoding": [
                    "gzip, deflate, br"
                ],
                "CloudFront-Forwarded-Proto": [
                    "https"
                ],
                "CloudFront-Is-Desktop-Viewer": [
                    "true"
                ],
                "CloudFront-Is-Mobile-Viewer": [
                    "false"
                ],
                "CloudFront-Is-SmartTV-Viewer": [
                    "false"
                ],
                "CloudFront-Is-Tablet-Viewer": [
                    "false"
                ],
                "CloudFront-Viewer-Country": [
                    "IN"
                ],
                "Content-Type": [
                    "application/json"
                ],
                "Host": [
                    "uap6yawi5d.execute-api.us-east-1.amazonaws.com"
                ],
                "Postman-Token": [
                    "461d11fd-df49-4572-8ab4-bd75d155577f"
                ],
                "User-Agent": [
                    "PostmanRuntime/7.26.5"
                ],
                "Via": [
                    "1.1 1e1845653f1116e06ee8f549030eac08.cloudfront.net (CloudFront)"
                ],
                "X-Amz-Cf-Id": [
                    "fRjOWCVKr7IaONi9X4U8-THOc3OElkUgHPmJOpdifXwMrTHKVBT6Eg=="
                ],
                "X-Amzn-Trace-Id": [
                    "Root=1-5fb7524d-606921ef41ca358e6768fc2a"
                ],
                "X-Forwarded-For": [
                    "157.49.217.6, 52.46.49.166"
                ],
                "X-Forwarded-Port": [
                    "443"
                ],
                "X-Forwarded-Proto": [
                    "https"
                ]
            },
            "queryStringParameters": {
                "query1": "12",
                "value1": "test value"
            },
            "multiValueQueryStringParameters": {
                "query1": [
                    "12"
                ],
                "value1": [
                    "test value"
                ]
            },
            "pathParameters": {
                "id": "12"
            },
            "stageVariables": None,
            "requestContext": {
                "resourceId": "9dmd8a",
                "resourcePath": "/ping",
                "httpMethod": "POST",
                "extendedRequestId": "WSnMKHCSIAMFxAA=",
                "requestTime": "20/Nov/2020:05:21:17 +0000",
                "path": "/dev/ping",
                "accountId": "533829049313",
                "protocol": "HTTP/1.1",
                "stage": "dev",
                "domainPrefix": "uap6yawi5d",
                "requestTimeEpoch": 1605849677778,
                "requestId": "478be0bb-d9b7-450f-955b-f4bf283b10b1",
                "identity": {
                    "cognitoIdentityPoolId": None,
                    "accountId": None,
                    "cognitoIdentityId": None,
                    "caller": None,
                    "sourceIp": "157.49.217.6",
                    "principalOrgId": None,
                    "accessKey": None,
                    "cognitoAuthenticationType": None,
                    "cognitoAuthenticationProvider": None,
                    "userArn": None,
                    "userAgent": "PostmanRuntime/7.26.5",
                    "user": None
                },
                "domainName": "uap6yawi5d.execute-api.us-east-1.amazonaws.com",
                "apiId": "uap6yawi5d"
            },
            "body": "----------------------------503769280530400724074437\r\nContent-Disposition: form-data; "
                    "name=\"message\"\r\n\r\nhello-world\r\n----------------------------503769280530400724074437\r"
                    "\nContent-Disposition: form-data; name=\"message1\"; "
                    "filename=\"helloworld.html\"\r\nContent-Type: "
                    "text/html\r\n\r\n<html>\r\n\t<head></head>\r\n\t<title></title>\r\n\t<body>hello "
                    "world</body>\r\n</html>\r\n----------------------------503769280530400724074437--\r\n",
            "isBase64Encoded": False
        }
        parser = AWSHttpParser(event)
        req = parser.parse_request()
        print(req.headers['Accept'])
        assert req.headers[
                   'Accept'] in 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
        assert req.params

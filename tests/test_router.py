from unittest import TestCase

from columbus.models import HttpResponse
from columbus.router import Router, HttpRequest, CloudAuthRouter


class TestRouter(TestCase):
    """
    GET
    {
    "resource": "/ping",
    "path": "/ping",
    "httpMethod": "GET",
    "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "CloudFront-Forwarded-Proto": "https",
        "CloudFront-Is-Desktop-Viewer": "true",
        "CloudFront-Is-Mobile-Viewer": "false",
        "CloudFront-Is-SmartTV-Viewer": "false",
        "CloudFront-Is-Tablet-Viewer": "false",
        "CloudFront-Viewer-Country": "IN",
        "Host": "uap6yawi5d.execute-api.us-east-1.amazonaws.com",
        "Postman-Token": "66616fb0-a73f-48fc-b9c1-46371d045bb2",
        "User-Agent": "PostmanRuntime/7.26.5",
        "Via": "1.1 9c7c2bcc2cb8136de33ca4d25c9defe2.cloudfront.net (CloudFront)",
        "X-Amz-Cf-Id": "nriUSiOuwGVZ9UQt8pFcOvM7qzRKGiJGqNSflDZSWoaybfBjArCNcQ==",
        "X-Amzn-Trace-Id": "Root=1-5fb75051-554a2a2f0bb989c0244e3267",
        "X-Forwarded-For": "157.49.217.6, 52.46.49.70",
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
        "Host": [
            "uap6yawi5d.execute-api.us-east-1.amazonaws.com"
        ],
        "Postman-Token": [
            "66616fb0-a73f-48fc-b9c1-46371d045bb2"
        ],
        "User-Agent": [
            "PostmanRuntime/7.26.5"
        ],
        "Via": [
            "1.1 9c7c2bcc2cb8136de33ca4d25c9defe2.cloudfront.net (CloudFront)"
        ],
        "X-Amz-Cf-Id": [
            "nriUSiOuwGVZ9UQt8pFcOvM7qzRKGiJGqNSflDZSWoaybfBjArCNcQ=="
        ],
        "X-Amzn-Trace-Id": [
            "Root=1-5fb75051-554a2a2f0bb989c0244e3267"
        ],
        "X-Forwarded-For": [
            "157.49.217.6, 52.46.49.70"
        ],
        "X-Forwarded-Port": [
            "443"
        ],
        "X-Forwarded-Proto": [
            "https"
        ]
    },
    "queryStringParameters": null,
    "multiValueQueryStringParameters": null,
    "pathParameters": null,
    "stageVariables": null,
    "requestContext": {
        "resourceId": "9dmd8a",
        "resourcePath": "/ping",
        "httpMethod": "GET",
        "extendedRequestId": "WSl80ED8oAMFXIg=",
        "requestTime": "20/Nov/2020:05:12:49 +0000",
        "path": "/dev/ping",
        "accountId": "533829049313",
        "protocol": "HTTP/1.1",
        "stage": "dev",
        "domainPrefix": "uap6yawi5d",
        "requestTimeEpoch": 1605849169987,
        "requestId": "dc786cc2-e875-44db-920b-eb83e0ea3c97",
        "identity": {
            "cognitoIdentityPoolId": null,
            "accountId": null,
            "cognitoIdentityId": null,
            "caller": null,
            "sourceIp": "157.49.217.6",
            "principalOrgId": null,
            "accessKey": null,
            "cognitoAuthenticationType": null,
            "cognitoAuthenticationProvider": null,
            "userArn": null,
            "userAgent": "PostmanRuntime/7.26.5",
            "user": null
        },
        "domainName": "uap6yawi5d.execute-api.us-east-1.amazonaws.com",
        "apiId": "uap6yawi5d"
    },
    "body": null,
    "isBase64Encoded": false
}
    """

    """
    {
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
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "uap6yawi5d.execute-api.us-east-1.amazonaws.com",
        "Postman-Token": "1d2ab9ae-1446-4a64-a69b-e2d12d454a6f",
        "User-Agent": "PostmanRuntime/7.26.5",
        "Via": "1.1 1e1845653f1116e06ee8f549030eac08.cloudfront.net (CloudFront)",
        "X-Amz-Cf-Id": "bnHCaGTJWj5scQj_aPFuIt1BT5i_j_4EmnSC6DJFTYhL44bDjRuUMQ==",
        "X-Amzn-Trace-Id": "Root=1-5fb75222-0ad57188523c717c3d044bab",
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
            "application/x-www-form-urlencoded"
        ],
        "Host": [
            "uap6yawi5d.execute-api.us-east-1.amazonaws.com"
        ],
        "Postman-Token": [
            "1d2ab9ae-1446-4a64-a69b-e2d12d454a6f"
        ],
        "User-Agent": [
            "PostmanRuntime/7.26.5"
        ],
        "Via": [
            "1.1 1e1845653f1116e06ee8f549030eac08.cloudfront.net (CloudFront)"
        ],
        "X-Amz-Cf-Id": [
            "bnHCaGTJWj5scQj_aPFuIt1BT5i_j_4EmnSC6DJFTYhL44bDjRuUMQ=="
        ],
        "X-Amzn-Trace-Id": [
            "Root=1-5fb75222-0ad57188523c717c3d044bab"
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
    "queryStringParameters": null,
    "multiValueQueryStringParameters": null,
    "pathParameters": null,
    "stageVariables": null,
    "requestContext": {
        "resourceId": "9dmd8a",
        "resourcePath": "/ping",
        "httpMethod": "POST",
        "extendedRequestId": "WSnFZFbxIAMFtMg=",
        "requestTime": "20/Nov/2020:05:20:34 +0000",
        "path": "/dev/ping",
        "accountId": "533829049313",
        "protocol": "HTTP/1.1",
        "stage": "dev",
        "domainPrefix": "uap6yawi5d",
        "requestTimeEpoch": 1605849634478,
        "requestId": "56cdcefc-7931-492e-8cf1-5e7557e47dcc",
        "identity": {
            "cognitoIdentityPoolId": null,
            "accountId": null,
            "cognitoIdentityId": null,
            "caller": null,
            "sourceIp": "157.49.217.6",
            "principalOrgId": null,
            "accessKey": null,
            "cognitoAuthenticationType": null,
            "cognitoAuthenticationProvider": null,
            "userArn": null,
            "userAgent": "PostmanRuntime/7.26.5",
            "user": null
        },
        "domainName": "uap6yawi5d.execute-api.us-east-1.amazonaws.com",
        "apiId": "uap6yawi5d"
    },
    "body": "message=helloworld",
    "isBase64Encoded": false
}
{
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
        "Content-Type": "application/json",
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
    "queryStringParameters": null,
    "multiValueQueryStringParameters": null,
    "pathParameters": null,
    "stageVariables": null,
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
            "cognitoIdentityPoolId": null,
            "accountId": null,
            "cognitoIdentityId": null,
            "caller": null,
            "sourceIp": "157.49.217.6",
            "principalOrgId": null,
            "accessKey": null,
            "cognitoAuthenticationType": null,
            "cognitoAuthenticationProvider": null,
            "userArn": null,
            "userAgent": "PostmanRuntime/7.26.5",
            "user": null
        },
        "domainName": "uap6yawi5d.execute-api.us-east-1.amazonaws.com",
        "apiId": "uap6yawi5d"
    },
    "body": "{\r\n    \"message\": \"hello-world\"\r\n}",
    "isBase64Encoded": false
}
    """

    def test_aws_parser(self):
        event = {
            "resource": "/ping",
            "path": "/ping",
            "httpMethod": "GET",
            "headers": {
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Authorization": "BEARER eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDU5NzMzNDYsImlhdCI6MTYwNTg4Njk0Niwic3ViIjoxMn0.OOpxHRNi_S_yAgkpG5S-MSpQy5PKsQap_IPBaTGlm_0",
                "CloudFront-Forwarded-Proto": "https",
                "CloudFront-Is-Desktop-Viewer": "true",
                "CloudFront-Is-Mobile-Viewer": "false",
                "CloudFront-Is-SmartTV-Viewer": "false",
                "CloudFront-Is-Tablet-Viewer": "false",
                "CloudFront-Viewer-Country": "IN",
                "Content-Type": "application/json",
                "Host": "uap6yawi5d.execute-api.us-east-1.amazonaws.com",
                "Postman-Token": "76b43604-97f1-4822-8ba5-517450833616",
                "User-Agent": "PostmanRuntime/7.26.5",
                "Via": "1.1 1e1845653f1116e06ee8f549030eac08.cloudfront.net (CloudFront)",
                "X-Amz-Cf-Id": "-VatJj1GZE4tIkY2TJ0OL8RTv3roaPB4_wiHePDzU_F692-ySqi-Hg==",
                "X-Amzn-Trace-Id": "Root=1-5fb75313-33afca8a7a39ebbc238b75f3",
                "X-Forwarded-For": "157.49.217.6, 52.46.49.146",
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
                "Authorization": [
                    ""
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
                    "76b43604-97f1-4822-8ba5-517450833616"
                ],
                "User-Agent": [
                    "PostmanRuntime/7.26.5"
                ],
                "Via": [
                    "1.1 1e1845653f1116e06ee8f549030eac08.cloudfront.net (CloudFront)"
                ],
                "X-Amz-Cf-Id": [
                    "-VatJj1GZE4tIkY2TJ0OL8RTv3roaPB4_wiHePDzU_F692-ySqi-Hg=="
                ],
                "X-Amzn-Trace-Id": [
                    "Root=1-5fb75313-33afca8a7a39ebbc238b75f3"
                ],
                "X-Forwarded-For": [
                    "157.49.217.6, 52.46.49.146"
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
                "resourceId": "8uxtlx",
                "resourcePath": "/ping",
                "httpMethod": "GET",
                "extendedRequestId": "WSnrDECnIAMFV0Q=",
                "requestTime": "20/Nov/2020:05:24:35 +0000",
                "path": "/dev/ping/12/",
                "accountId": "533829049313",
                "protocol": "HTTP/1.1",
                "stage": "dev",
                "domainPrefix": "uap6yawi5d",
                "requestTimeEpoch": 1605849875439,
                "requestId": "dfcd1c05-dc6c-4bc0-9a84-fa968d16665a",
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
            "body": "{\r\n    \"message\": \"hello-world\"\r\n}",
            "isBase64Encoded": False
        }
        app = CloudAuthRouter()

        @app.get('/ping')
        def test_hello(req: HttpRequest):
            print(req.headers)
            print(req.get_context('userinfo'))
            # assert req.body == {}
            # assert req.headers in {'Access-Control-Allow-Origin'}
            # assert req.get_context('userinfo') == '12'
            return "hello-world"

        app.get_router()(event)

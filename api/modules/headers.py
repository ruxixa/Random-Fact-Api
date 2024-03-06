from flask import request, abort

# function to check request header
def check_headers():                                         
    headers = dict(request.headers)     
    content_type = headers.get("Content-Type")  

    if not content_type or content_type != "application/json":      # checking is request an application
        abort(403)
    
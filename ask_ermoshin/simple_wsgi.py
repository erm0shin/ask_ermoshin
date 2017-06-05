def simple_app(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]

    query_string_list = environ['QUERY_STRING'].split("&")
    get_params = [bytes(str(param) + "\t", "utf-8") for param in query_string_list]

    length = int(environ.get('CONTENT_LENGTH', '0'))
    post_params = environ['wsgi.input'].read(length)

    body = [bytes('Hello, world!\n', "utf-8")] + get_params + [bytes("\n", "utf-8")] + [bytes(param) + "\t" for param in
                                                                                        post_params]
    start_response(status, headers)
    return body

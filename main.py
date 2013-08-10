# https://code.google.com/p/httplib2/wiki/Examples
import thirdparty.httplib2

def main(url):
    conn = thirdparty.httplib2.Http(".cache")
    resp, content = conn.request(url, "GET")
    print(resp)

if __name__ == '__main__':
    main("http://www.google.com/")
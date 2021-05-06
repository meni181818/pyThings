#GNU General Public License v3.0

#prameter the_url as string, url address
def get_url_size(the_url):
    import urllib.request
    
    #request the head
    req_head = urllib.request.Request(the_url, method='HEAD')
    #open the req_head (http object)
    open_head = urllib.request.urlopen(req_head)
    #return the size (string to integer)
    return int(open_head.headers['Content-Length'])
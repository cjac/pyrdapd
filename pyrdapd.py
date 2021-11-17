import pprint
import re

pp = pprint.PrettyPrinter(indent=4)

def application(env, start_response):
    pp.pprint(env)

    m = re.search('^/(ip|autnum|domain|nameserver|entity)/(.+)', env['PATH_INFO'])

    print( m.group(1) )

    if m.group(1) == 'ip':
        start_response('501 Not Implemented', [('Content-Type','text/html')])
        return [b"IP requested\n"]

    if m.group(1) == 'autnum':
        start_response('501 Not Implemented', [('Content-Type','text/html')])
        return [b"AS requested\n"]

    if m.group(1) == 'domain':
        start_response('501 Not Implemented', [('Content-Type','text/html')])
        return [b"Domain requested\n"]

    if m.group(1) == 'nameserver':
        start_response('501 Not Implemented', [('Content-Type','text/html')])
        return [b"Nameserver requested\n"]

    if m.group(1) == 'entity':
        start_response('501 Not Implemented', [('Content-Type','text/html')])
        return [b"Entity requested\n"]

    else:
        start_response('200 OK', [('Content-Type','text/html')])
        return [b"Hello World\n"]

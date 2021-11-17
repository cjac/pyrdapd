import pprint
import re

pp = pprint.PrettyPrinter(indent=4)

def application(env, start_response):
    pp.pprint(env)

    m = re.search('^/(ip|autnum|domain|nameserver|entity)/(.+)', env['PATH_INFO'])

    segment = m.group(1)
    reference = m.group(2)

    print( m.group(1) )

    if segment == 'ip':
        start_response('501 Not Implemented', [('Content-Type','text/html')])
        return [b"IP requested\n"]

    elif segment == 'autnum':
        start_response('501 Not Implemented', [('Content-Type','text/html')])
        return [b"AS requested\n"]

    elif segment == 'domain':
        start_response('501 Not Implemented', [('Content-Type','text/html')])
        return [b"Domain requested\n"]

    elif segment == 'nameserver':
        start_response('501 Not Implemented', [('Content-Type','text/html')])
        return [b"Nameserver requested\n"]

    elif segment == 'entity':
        start_response('501 Not Implemented', [('Content-Type','text/html')])
        return [b"Entity requested\n"]

    else:
        start_response('200 OK', [('Content-Type','text/html')])
        return [b"Hello World\n"]

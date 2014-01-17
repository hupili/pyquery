'''
CLI for pyquery

Usage:
    pyquery <selector>
    pyquery <selector> -p <projector>
'''

import sys
import docopt
from pyquery import PyQuery as pq

# The workflow is driven by iterator/generator

def array_output(a):
    for i in a:
        if i:
            sys.stdout.write(str(i) + '\n')

def project(a, projector):
    # For initial version, only support grepping one field.
    # Support multiple fields if there are good use cases.
    #fields = set(projector.split(','))
    for i in a:
        yield i.get(projector, None)

def html_element_to_dict(a):
    for i in a:
        d = {}
        d['tag'] = i.tag
        d['text'] = i.text
        d.update(i.attrib)
        yield d

if __name__ == '__main__':
    args = docopt.docopt(__doc__)
    html = sys.stdin.read()
    d = pq(html)
    matches = d(args['<selector>'])
    data = html_element_to_dict(matches)
    if args['<projector>']:
        data = project(data, args['<projector>'])
    array_output(data)


#!/usr/bin/env python

import sys, socket
import json
import time

ip = socket.gethostbyname('morbo')
s = socket.create_connection((ip, 9090))

def ins(d):
    j='{ "jsonrpc": "2.0", "method": "JSONRPC.Introspect", "params": { "filter": { "id": "%s", "type": "method" } }, "id": 1 }' % (d)
    s.send(j)
    pretty(s.recv(4096))

def rq(d, params):
    p = json.dumps(params)
    j='{ "jsonrpc": "2.0", "method": "'+d+'", "params": '+p+', "id": 1 }'
    print j+'\n'
    s.send(j)
    return s.recv(4096)

def pretty(text):
    i = json.loads(text)
    print json.dumps(i, sort_keys=True, indent=4, separators=(',', ': '))

def whore():
    #ins('Player.Open')

    # play file
    print rq('Player.Open', { \
        'item': { 'file' : "/some/path/Sandstorm.mp4" }, \
    })

    # put xbmc in play mode
    print rq('Player.PlayPause', { \
            'playerid': 1,
            'play': True
    })

    # full volume
    print rq('Application.SetVolume', { \
            'volume': 100
    })

    #time.sleep()


    # seek to some point
    print rq('Player.Seek', {\
            'playerid': 1,
            'value': { 'hours': 0, 'minutes': 0, 'seconds': 27, 'milliseconds': 0 }
    })

if __name__ == "__main__":
    whore()


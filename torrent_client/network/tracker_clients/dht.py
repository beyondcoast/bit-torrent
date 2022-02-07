import asyncio
import logging
import random
import struct
import socket
import urllib.parse
from enum import Enum
from typing import Optional

from torrent_client.models import DownloadInfo
from torrent_client.network.tracker_clients.base import BaseTrackerClient
from torrent_client.network.tracker_clients.base import BaseTrackerClient, EventType, TrackerError, \
    parse_compact_peers_list

# TODO: Use the other tracker clients as a model to integrate the Kademlia stuff

# FIXME: These are hardcoded values until the actual peer list is working
PEER_HOST = "127.0.0.1"
PEER_PORT = 1337
PEER_LIST = [(PEER_HOST, PEER_PORT)]

def to_compact_form(ip, port):
    host = socket.inet_aton(ip)
    compact_host = struct.pack("!4sH", host, port)
    return compact_host


# This little silliness to make a compact peer list is just so we can sanity check
#   the format until we're actually getting it from another peer.
compact_peer_list = b""
for ip, port in PEER_LIST:
    compact_peer_list += to_compact_form(ip, port)

#PEERLIST = parse_compact_peers_list(
"""
    def from_compact_form(cls, data: bytes):
        ip, port = struct.unpack('!4sH', data)
        host = socket.inet_ntoa(ip)
        return cls(host, port)
"""

class DHTTrackerClient(BaseTrackerClient):
    #def __init__(self, bootstrap_peerlist):
    def __init__(self, url: urllib.parse.ParseResult, download_info: DownloadInfo, our_peer_id: bytes,
                 *, loop: asyncio.AbstractEventLoop=None):
        super().__init__(download_info, our_peer_id)

        if url.scheme != 'dht':
            raise ValueError('TrackerUDPClient expects announce_url with UDP protocol')

        # TODO: Actually do a Kademlia query here?
        self._peers = parse_compact_peers_list(compact_peer_list)
        print(self._peers)
        #peers = self.parse_compact_peers_list(bootstrap_peerlist)

    async def announce(self, server_port: int, event: EventType):
        pass

if __name__ == "__main__":
    import code
    code.interact(local=locals())

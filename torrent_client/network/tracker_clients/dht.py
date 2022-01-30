

# TODO: Use the other tracker clients as a model to integrate the Kademlia stuff

class DHTTrackerClient(BaseTrackerClient):
    def __init__(self, bootstrap_peerlist):
        peers = self.parse_compact_peers_list(bootstrap_peerlist)


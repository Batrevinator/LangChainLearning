# Imports here

class Location:
    
    def __init__(self, name: str, address: str, type: str):
        self.neigbors = {}
        self.name = name
        self.address = address
        self.type = type  # e.g., 'store', 'home'
    
    def addNeighbor(self, neighbor_location: "Location", distance: float):
        self.neigbors[neighbor_location] = distance
        neighbor_location.neigbors[self] = distance
        
    def getNeighbors(self):
        return self.neigbors
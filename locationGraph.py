# Includes
import db_utils as db
from location import Location
import random

class LocationGraph:
    def __init__(self, graph: dict = None):
        self.graph = graph
        
    def show_graph(self):
        return_string = ""
        for location, neighbors in self.graph.items():
            return_string.join(f"Location: {location.name} ({location.type})")
            for neighbor, distance in neighbors:
                return_string.join(f"  Neighbor: {neighbor.name} ({neighbor.type}), Distance: {distance:.2f}")
            return_string.join("\n")
        return return_string
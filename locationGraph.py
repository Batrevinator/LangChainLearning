# Includes
import db_utils as db
from location import Location
import random

class LocationGraph:
    def __init__(self, graph: dict = None):
        self.graph = graph
        self.master_location_list: list[Location] = list(graph.keys()) if graph else []
        
        
    def show_graph(self):
        return_string = ""
        for location in self.master_location_list:
            return_string += ("------------------------------\n")
            return_string += (f"Location: {location.name} ({location.type}):\n")
            for neighbor, distance in location.getNeighbors().items():
                return_string += (f"  Neighbor: {neighbor.name} ({neighbor.type}), Distance: {distance:.2f}\n")
        return return_string
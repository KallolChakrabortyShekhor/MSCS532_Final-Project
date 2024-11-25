import heapq
import math

# Optimized Graph Representation for Road Network
class RoadNetwork:
    def __init__(self):
        self.graph = {}  # Adjacency list representation
        self.precomputed_paths = {}  # For caching shortest paths

    def add_intersection(self, intersection):
        """Add an intersection (node) to the road network."""
        if intersection not in self.graph:
            self.graph[intersection] = []

    def add_road(self, intersection1, intersection2, traffic_weight=1):
        """Add a road (edge) between two intersections with a given traffic weight."""
        if intersection1 in self.graph and intersection2 in self.graph:
            self.graph[intersection1].append((intersection2, traffic_weight))
            self.graph[intersection2].append((intersection1, traffic_weight))  # Assuming undirected roads
        else:
            raise ValueError("Both intersections must exist in the road network.")

    def dijkstra(self, start):
        """Compute shortest paths from the start node using Dijkstra's algorithm."""
        distances = {node: math.inf for node in self.graph}
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

    def precompute_paths(self, start):
        """Precompute shortest paths from a given intersection."""
        self.precomputed_paths[start] = self.dijkstra(start)

    def get_shortest_path(self, start, end):
        """Retrieve the shortest path between two intersections."""
        if start not in self.precomputed_paths:
            self.precompute_paths(start)
        return self.precomputed_paths[start].get(end, math.inf)

# Optimized Priority Queue for Real-Time Traffic Events
class TrafficEventQueue:
    def __init__(self):
        self.queues = {}  # Dictionary of priority queues for geographic sharding

    def add_event(self, zone, priority, event_details):
        """Add a traffic event to the queue with a given priority."""
        if zone not in self.queues:
            self.queues[zone] = []
        heapq.heappush(self.queues[zone], (priority, event_details))

    def get_next_event(self, zone):
        """Get the next traffic event from the queue."""
        if zone in self.queues and self.queues[zone]:
            return heapq.heappop(self.queues[zone])
        return None

# Optimized Hash Table for Quick Data Lookup
class IntersectionData:
    def __init__(self):
        self.data = {}
        self.cache = {}  # Cache for frequently accessed intersections

    def add_data(self, intersection, details):
        """Add or update data for a specific intersection."""
        self.data[intersection] = details

    def get_data(self, intersection):
        """Retrieve data for a specific intersection."""
        if intersection in self.cache:
            return self.cache[intersection]
        data = self.data.get(intersection, "No data available")
        self.cache[intersection] = data
        return data

# Test Script for the Optimized System
if __name__ == "__main__":
    # Initialize Components
    road_network = RoadNetwork()
    traffic_events = TrafficEventQueue()
    intersection_data = IntersectionData()

    # Build Road Network
    road_network.add_intersection("A")
    road_network.add_intersection("B")
    road_network.add_intersection("C")
    road_network.add_road("A", "B", 5)
    road_network.add_road("B", "C", 3)
    road_network.add_road("A", "C", 8)

    # Precompute shortest paths
    road_network.precompute_paths("A")
    print("Shortest path from A to C:", road_network.get_shortest_path("A", "C"))

    # Add Intersection Data
    intersection_data.add_data("A", {"signal_status": "green", "traffic_flow": 20})
    intersection_data.add_data("B", {"signal_status": "red", "traffic_flow": 10})

    # Retrieve and print data
    print("Intersection Data (A):", intersection_data.get_data("A"))
    print("Intersection Data (B):", intersection_data.get_data("B"))

    # Add Traffic Events by Zone
    traffic_events.add_event("Zone1", 1, "Accident reported at Intersection A")
    traffic_events.add_event("Zone1", 2, "High traffic on Road A-B")

    # Process Events
    print("Next Traffic Event in Zone1:", traffic_events.get_next_event("Zone1"))
    print("Next Traffic Event in Zone1:", traffic_events.get_next_event("Zone1"))

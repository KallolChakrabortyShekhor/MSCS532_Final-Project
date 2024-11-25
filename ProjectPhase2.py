# Graph Representation for Road Network
class RoadNetwork:
    def __init__(self):
        self.graph = {}  # Adjacency list representation

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

    def display_network(self):
        """Display the road network."""
        return self.graph


# Priority Queue for Real-Time Traffic Events
import heapq

class TrafficEventQueue:
    def __init__(self):
        self.queue = []  # List to store events

    def add_event(self, priority, event_details):
        """Add a traffic event to the queue with a given priority."""
        heapq.heappush(self.queue, (priority, event_details))

    def get_next_event(self):
        """Get the next traffic event from the queue."""
        return heapq.heappop(self.queue) if self.queue else None

    def is_empty(self):
        """Check if the event queue is empty."""
        return len(self.queue) == 0


# Hash Table for Quick Data Lookup
class IntersectionData:
    def __init__(self):
        self.data = {}

    def add_data(self, intersection, details):
        """Add or update data for a specific intersection."""
        self.data[intersection] = details

    def get_data(self, intersection):
        """Retrieve data for a specific intersection."""
        return self.data.get(intersection, "No data available")


# Test Script to Demonstrate Core Functionalities
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

    # Add Intersection Data
    intersection_data.add_data("A", {"signal_status": "green", "traffic_flow": 20})
    intersection_data.add_data("B", {"signal_status": "red", "traffic_flow": 10})

    # Add Traffic Events
    traffic_events.add_event(1, "Accident reported at Intersection A")
    traffic_events.add_event(2, "High traffic on Road A-B")

    # Demonstrate Key Functionalities
    print("Road Network:", road_network.display_network())
    print("Intersection Data (A):", intersection_data.get_data("A"))
    print("Intersection Data (B):", intersection_data.get_data("B"))
    print("Next Traffic Event:", traffic_events.get_next_event())
    print("Next Traffic Event:", traffic_events.get_next_event())
    print("Is Traffic Event Queue Empty:", traffic_events.is_empty())

class Node:
    """ A class used to represent a user
        
        Attributes:
        -----------
        value (int): user's name
        neighbours (list of Node): user's friends
    """

    def __init__(self, value, neighbours):
        self.value = value
        self.neighbours = neighbour

    def __repr__(self):
        return f"node: {self.value} -> neighbours: {' '.join([str(neighbour.value) for neighbour in self.neighbours])}"


class Graph:
    """ A class used to represents the social network

        Attributes:
        ----------
        nodes (list of Node): the users using the social network
    """

    def __init__(self):
        self.nodes = []

    def find_node(self, value):
        """Method that checks if a Node with a given value exists in the graph  

        Args:
            value (int): the searched node's value

        Returns:
            The maching Node if it exists in the graph, None otherwise
        """
        if matching_nodes := [node for node in self.nodes if node.value == value]:
            return matching_nodes[0]
        return None
    
    def bfs(self, start, end):
        """Method that finds the shortest path between a start node and an end node using Breadth First Search algorithm

        Args:
            start (Node): start node
            end (Node): end node

        Returns:
            list: the path between the start node and the end node
        """
        
        queue = [start]

        # list that keeps track of the visited nodes
        visited = [start]

        # dictionary(Node, Node) where the key = node and the value = node's parent
        parents = {start: None}

        while queue:
            current_node = queue.pop(0)

            if current_node == end_node:
                route = []
                while current_node:
                    route.append(current_node.value)
                    current_node = parents[current_node]

                return route[::-1]
            else:
                for node in current_node.neighbours:
                    if node not in visited:
                        visited.append(node)
                        parents[node] = current_node
                        queue.append(node)


def read_input():
    """_summary_
        Function that reads the input arguments as it follows:
            first line: n = number of nodes in the graph
            second line: start end = the values of the start node and the end node
            next lines: the adjacency list
    Returns:
        If no exception occured and the input data is valid:
            start_node: Node
            end_node: Node
            graph: Graph
        Else:
            None
    """
    try:
        with open("input.txt", "r") as f:
            n = int(f.readline())
            if n < 2:
                print("Number of nodes must be at least equal to 2")
                return None

            line = f.readline().split()
            start, end = int(line[0]), int(line[1])

            if not (0 <= start < n and 0 <= end < n):
                print("At least one of the input nodes is invalid")
                return None 

            #initially the graph's nodes don't have any neighbours
            graph = Graph()
            graph.nodes = [Node(i, []) for i in range(n)]

            for line in f:
                node_value, node_neighbours = line.split(":")
                node = graph.find_node(int(node_value))
                node.neighbours = [graph.find_node(int(x)) for x in node_neighbours.split(",")]

            return graph.find_node(start), graph.find_node(end), graph
    except Exception as e:
        print(f"Exception: {e}")
        return None


if __name__ == "__main__":
    result = read_input()

    if result != None:
        start_node, end_node, graph = result

        route = graph.bfs(start_node, end_node)
        if route is None:
            print(f"Users {start_node.value} and {end_node.value} don't have any friends in common")
        else:
            print(route)
            print(f"Length of the shortest chain of friends: {len(route) - 1}")
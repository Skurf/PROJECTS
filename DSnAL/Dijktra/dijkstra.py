# import priorityqueue
from priorityqueue import priorityQueue
from graph import Graph
from vertex import Vertex
from edge import Edge

def dijkstra(graph,start):

  # Initialize the 'distances','previous' and 'visited' containers
    previous = {v: None for v in Graph.adjacency_list.keys()}
    visited = {v:False for v in Graph.adjacency_list.keys()}
    distances = {v: float('inf') for v in Graph.adjacency_list.keys()}
  # Set the distance for the starting vertex to 0
    distances[start] = 0
  # Create a priority queue and add the start vertex and its distance
    queue = priorityQueue()
    queue.add_task(0,start)
  # Start a loop for as long as there's something in the queue
    while queue:
  #   Pop from the queue, saving the vertex and its distance
      removed_distance, removed = queue.pop_task()
      visited[removed] = True
      for edge in Graph.adjacency_list[removed]:
        if visited[edge.vertex]:
          continue
        new_distance = removed_distance + edge.distance
        if new_distance < distances[edge.vertex]:
          distances[edge.vertex] = new_distance
          previous[edge.vertex] = removed
          queue.add_task(new_distance,edge.vertex)
    return

def main():
  adjacency_list = {
    A:[B,C,D],
    B:[A,C,E],
    C:[A,B,E,F],
    D:[A,F],
    E:[B,C,F],
    F:[C,D,E]
  }
  result = dijkstra(adjacency_list,A)
  print(result)

#   Mark the removed vertex as visited
#   Start a loop over all the neighbors of the removed vertex
#   if the current vertex is visited, skip to the next
#   otherwise calculate the distance to it
#   if the new distance is smaller
#     update distances table
#     update previous table
#     push into the queue the neighbor and its distances



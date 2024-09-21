import heapq
import itertools

class priorityQueue:
  def __init__(self):
    self.pq= []
    self.entry_finder = {}
    self.counter = itertools.count()
  
  def __len__(self):
    return len(self.pq)
  
  def add_task(self,priority,task):
    'add a new task or update the priority of an existing task'
    if task in self.entry_finder:
      self.update_priority(priority,task)
      return self
    count = next(self.counter)
    entry = [priority,count,task]
    self.entry_finder[task] = entry
    heapq.heappush(self.pq,entry)

  def update_priority(self,priority,task):
    'update the priority of a task, raise keyError if not found'
    entry = self.entry_finder[task]
    count= next(self.counter)
    entry[0],entry[1] = priority,task

  def pop_task(self):
    'remove and return the lowest priority task, raise keyError if empty'
    while self.pq:
      priority,count,task = heapq.heappop(self.pq)
      del self.entry_finder[task]
      return priority,task
    raise KeyError('pop from an empty priority queue')
class graph:
   def __init__(self,gdict=None):
      if gdict is None:
         gdict = []
      self.gdict = gdict
   # Get the keys of the dictionary
   def getVertices(self):
      return list(self.gdict.keys())
   
   def get_neighbours(self, vertex):
    if vertex not in self.gdict.keys(): 
         raise Exception("graph does not have this vertex")
    return list(self.gdict[vertex][1].keys())

   def get_neighbours_cost(self, vertex):
      if vertex not in self.gdict.keys(): 
            raise Exception("graph does not have vertex ", vertex)
      # return a list of cost in the same order as neighbours
      return self.gdict[vertex][1]
   
   def get_heuristic(self, vertex):
      if vertex not in self.gdict.keys(): 
            raise Exception("graph does not have vertex ", vertex)
      # return a list of cost in the same order as neighbours
      return self.gdict[vertex][0]

# Create the dictionary with graph elements
graph_elements = { 
   #node:  (heuristice, {neighbours:cost})
   "a" : (0, {"b":0,"c":0}),
   "b" : (0, {"a":0, "d":0}),
   "c" : (0, {"a":0, "d":0}),
   "d" : (0, {"e":0}),
   "e" : (0, {"d":0})
}
g = graph(graph_elements)
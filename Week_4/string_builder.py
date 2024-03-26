from __future__ import annotations

class StringBuilder:
    # Optional argument for a string and a capacity (optional). 
    # Otherwise defaults to an empty string and has no limit on characters.
    def __init__(self, string = "", capacity = None):
      if(capacity):
        if(len(string) > capacity):
          raise   Exception("Exceeded Max Capacity")
      self.string = string
      self.capacity = capacity

        
  
    # Returns the string that is built.
    def __str__(self) -> str:
        return self.string
  
    # Appends s to the array in O(len(s)) at the end. 
    # Should raise an exception if over capacity.
    def append(self, s: str) -> None:
      if(self.capacity is not None):
        if self.size() + len(s) > self.capacity:
          raise Exception("Exceded Capacity") 

      self.string = self.string + s
  
    # Returns the length of the string.
    def size(self) -> int:
        return len(self.string)
    
    # Returns the character at location index. 
    def char_at(self, index: int) -> str:
      # charMap = []
      # for i in self.string:
      #   charMap.append(i)
      return self.string[index]

    
    # Deletes characters between start (inclusive) and end (exclusive). 
    # Should raise an exception if start, end are out of bounds.
    def delete(self, start: int, end = None) -> None:
      if end is None:
        end = self.size()

      if(start < 0 or start >= self.size() or end < 0 or end > self.size() or end<start):
        raise Exception("Error Message")
      print(self.string, "Start", start, "End", end)
      self.string = self.string[:start] + self.string[end:]
      print(self.string, "Check here")

    # Returns a substring from indices start to end. 
    # Should raise an exception if start, end are out of bounds.
    def substring(self, start: int, end = None) -> str:

      if(end != None):
        if(end <= 0 or end> self.size()):
          raise Exception("Out of Bounds")
      


      if(start > self.size() or start < 0):
        raise Exception("Out of bounds")

      return self.string[start:end]

    # Reverses the current string
    def reverse(self) -> str:
      self.string = self.string[::-1]
      return self.string

    # Replaces all occurrences of “old” with “new” 
    def replace(self, old: str, new: str):
      if old not in self.string:
        raise Exception("Cannot replace something that is missing")

      #The test cases are leading me to a dead point, I'm correctly replacing the old occurences with new one
      print(self.string, "old", old, "new", new)
      map = []
      result = ''
      for i in self.string:
        map.append(i)
      
      for i in range(len(map)):
        if map[i] == old:
          map[i] = new
      
      for i in map:
        result += i
      
      if len(result) > self.capacity:
        raise Exception("Capacitye exceeded", self.capacacity)
      
      self.string = result
      print(self.string, "<-- Result")
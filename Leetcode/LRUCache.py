from collections import OrderedDict
''' Note: OrderedDict is dict subclass remembers the order in 
which keys are added to the dictionary. 
''' 

class LRUCache: 
	def __init__(self, capacity):
		self.capacity = capacity 
		self.cache = OrderedDict() 
		
		
	def get(self, key):
		'''  
		Check if the key exists first, if so then retrieve the value. 
		If key does not exist, then output -1.  

		- go through the OrderedDict(), checking if the key exists 
		'''
		if(key not in self.cache):
			return -1 
		else:
			'''place the key at the back of the cache. Then, return
			the value'''
			self.cache.move_to_end(key)
			return self.cache[key] 
 	

	def getCacheContent(self):
		return self.cache

	
	def put(self, key, value): 
		'''   
		purpose: Update the value of the key if the key exists, update 
		the value of the key. Otherwise, add the key-value pair to the cache.   

		- go through the cache, checking if the key exists. If it does, 
		then update the value of the key. 
		- if not, then add that key-value pair to cache. 
		- if we are trying to add a key to cache (and it already doesnt exist), 
		AND the length of cache exceeds the capcity of the cache, 
		then we evict the LRU key. 
		'''  
		
		if(key not in self.cache): 

			if(len(self.cache) >= self.capacity):
				#evict the key from cache 
				self.cache.popitem(last = False) 
		else:
			self.cache.move_to_end(key)
		#update the value of the key 
		self.cache[key] = value 


			

firstCache = LRUCache(2) 
firstCache.put(1, 1)
firstCache.put(2, 2) 
print(firstCache.getCacheContent())
print(firstCache.get(1))



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
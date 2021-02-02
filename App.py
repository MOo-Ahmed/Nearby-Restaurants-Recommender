import Engine
import time

start = time.time()

item = [30.11326325377716, 31.314122387609522]
n = 10
name = 'nearby-restaurants'
engine = Engine.RecommendationEngine(item, n, name)
engine.run()

end = time.time()

# total time taken
print(f"Time =  {end - start} seconds")


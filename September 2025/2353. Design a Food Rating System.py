class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_info = {}
        self.cuisine_ratings = defaultdict(list)

        for i in range(len(foods)):
            food, cuisine, rating = foods[i], cuisines[i], ratings[i]
            
            # Store food details for O(1) lookup
            self.food_info[food] = [cuisine, rating]
            
            # Push food info to the corresponding cuisine's max-heap
            heapq.heappush(self.cuisine_ratings[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_info[food][0]
        
        self.food_info[food][1] = newRating
        heapq.heappush(self.cuisine_ratings[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while True:
            # Get the top element from the max-heap for the cuisine
            top_rating, top_food = self.cuisine_ratings[cuisine][0]
            
            if -top_rating == self.food_info[top_food][1]:
                return top_food
            else:
                heapq.heappop(self.cuisine_ratings[cuisine])



# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.price = {}  # (shop, movie) -> price
        self.movie_to_unrented = {}  # movie -> SortedList of (price, shop)
        self.rented = SortedList()  # (price, shop, movie)
        
        for shop, movie, p in entries:
            self.price[(shop, movie)] = p
            if movie not in self.movie_to_unrented:
                self.movie_to_unrented[movie] = SortedList()
            self.movie_to_unrented[movie].add((p, shop))
    
    def search(self, movie: int) -> List[int]:
        if movie not in self.movie_to_unrented:
            return []
        return [shop for _, shop in self.movie_to_unrented[movie][:5]]
    
    def rent(self, shop: int, movie: int) -> None:
        p = self.price[(shop, movie)]
        # Remove from unrented
        self.movie_to_unrented[movie].remove((p, shop))
        # Add to rented
        self.rented.add((p, shop, movie))
    
    def drop(self, shop: int, movie: int) -> None:
        p = self.price[(shop, movie)]
        # Remove from rented
        self.rented.remove((p, shop, movie))
        # Add back to unrented
        self.movie_to_unrented[movie].add((p, shop))
    
    def report(self) -> List[List[int]]:
        return [[shop, movie] for p, shop, movie in self.rented[:5]]



# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()

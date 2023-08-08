from heap import MaxHeap


class Star:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    @property
    def distance(self):
        return (self.x**2 + self.y**2 + self.z**2)**(1/2)

    def __gt__(self, _obj: "Star"):
        return self.distance > _obj.distance

    def __ge__(self, _obj: "Star"):
        return self.distance >= _obj.distance

    def __lt__(self, _obj: "Star"):
        return self.distance < _obj.distance

    def __le__(self, _obj: "Star"):
        return self.distance <= _obj.distance
    
    def __repr__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"


def compute_k_closest_stars(stars, k):
    heap = MaxHeap()
    for star in stars:
        heap.heappush(star)
        if len(heap) > k:
            heap.heappop()
    closest_stars = []
    while heap:
        closest_stars.append(heap.heappop())
    return closest_stars


def main():
    stars = [Star(2,4,5),Star(8,1,0),Star(1,1,1),Star(6,1,8),Star(5,0,0),Star(-1,-7,0),Star(-4,9,10),Star(0,1,1),Star(3,1,8),Star(2,6,7)]
    k = 4
    print(compute_k_closest_stars(stars, k))


if __name__ == "__main__":
    main()

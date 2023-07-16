"""Check if 2 rectangles intersect"""


class Rectangle:
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width


def are_rectangles_intersecting(r1: Rectangle, r2: Rectangle):
    return (
        ((r1.x + r1.width) >= r2.x)
        and ((r2.x + r2.width) >= r1.x)
        and ((r1.y + r1.height) >= r2.y)
        and ((r2.y + r2.height) >= r1.y)
    )


def get_intersecting_rectangle(r1: Rectangle, r2: Rectangle):
    if are_rectangles_intersecting(r1, r2):
        return Rectangle(max(r1.x, r2.x), max(r1.y, r2.y), min(r1.height, r2.height), min(r1.width, r2.width))
    else:
        return None

# Variants
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __eq__(self, point: "Point") -> bool:
        return self.x == point.x and self.y == point.y and self.z == point.z


class RectangleNew:
    def __init__(self, p1: Point, p2: Point, p3: Point, p4: Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4


def are_points_on_same_plane(p1: Point, p2: Point, p3: Point, p4: Point):
    return (p1.x == p2.x == p3.x == p4.x) or (p1.y == p2.y == p3.y == p4.y) or (p1.z == p2.z == p3.z == p4.z)


def calculate_distance(p1: Point, p2: Point):
    return ((p1.x-p2.x)**2 + (p1.y-p2.y)**2 + (p1.z-p2.z)**2)**(1/2)


def are_all_points_different(p1: Point, p2: Point, p3: Point, p4: Point):
    return p1 != p2 and p1 != p3 and p1 != p4 and p2 != p3 and p2 != p4 and p3 != p4


def are_points_vertices_of_a_rectangle(p1: Point, p2: Point, p3: Point, p4: Point):
    if not are_points_on_same_plane(p1, p2, p3, p4):
        return False
    if not are_all_points_different(p1, p2, p3, p4):
        return False
    p1p2 = calculate_distance(p1, p2)
    p2p3 = calculate_distance(p3, p2)
    p3p4 = calculate_distance(p3, p4)
    p1p4 = calculate_distance(p1, p4)
    p1p3 = calculate_distance(p3, p1)
    p2p4 = calculate_distance(p4, p2)

    counter = {}
    for i in [p1p2, p1p3, p1p4, p2p3, p2p4, p3p4]:
        if i in counter: counter[i] += 1
        else: counter[i] = 1
    
    num_keys = len(list(counter.keys()))
    if num_keys > 3 or num_keys < 2: return False        

    values = list(counter.values())
    if num_keys == 3:
        return values == [2, 2, 2]
    else:
        return values == [2, 4] or values == [4, 2]


def are_rectangle_intersecting_any_orentation(r1: Rectangle, r2: Rectangle):
    raise NotImplementedError


def main():
    rectangle1 = Rectangle(0, 0, 3, 4)
    rectangle2 = Rectangle(1, 1, 2, 2)
    print(get_intersecting_rectangle(rectangle1, rectangle2).__dict__)

    p1, p2, p3, p4 = Point(0, 0, 0), Point(0, 4, 0), Point(2, 4, 0), Point(2, 0, 0)
    print(are_points_vertices_of_a_rectangle(p1, p2, p3, p4))

    rectangle1 = RectangleNew(p1, p2, p3, p4)
    rectangle2 = RectangleNew(p1, p2, p3, p4)
    print(are_rectangle_intersecting_any_orentation(rectangle1, rectangle2).__dict__)

if __name__ == "__main__":
    main()

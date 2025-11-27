import math

# Global constant for floating point comparisons
EPSILON = 1e-9

class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def distance_to(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def scale(self, factor, origin):
        self.x = origin.x + (self.x - origin.x) * factor
        self.y = origin.y + (self.y - origin.y) * factor

    def rotate(self, angle_rad, origin):
        ox, oy = origin.x, origin.y
        px, py = self.x, self.y

        qx = ox + (px - ox) * math.cos(angle_rad) - (py - oy) * math.sin(angle_rad)
        qy = oy + (px - ox) * math.sin(angle_rad) + (py - oy) * math.cos(angle_rad)

        self.x, self.y = qx, qy

    def __repr__(self):
        return f"Point({self.x:.6f}, {self.y:.6f})"


class Line:
    def __init__(self, p1=None, p2=None, a=None, b=None, c=None):
        if p1 is not None and p2 is not None:
            if abs(p1.x - p2.x) < EPSILON and abs(p1.y - p2.y) < EPSILON:
                raise ValueError("p1 and p2 must be distinct points to define a line.")
            # a x + b y + c = 0
            self.a = p1.y - p2.y
            self.b = p2.x - p1.x
            self.c = - (self.a * p1.x + self.b * p1.y)
        elif a is not None and b is not None and c is not None:
            if abs(a) < EPSILON and abs(b) < EPSILON:
                raise ValueError("At least one of a or b must be non-zero for a valid line.")
            self.a, self.b, self.c = float(a), float(b), float(c)
        else:
            raise ValueError("Line must be initialized with two points or coefficients a, b, c.")

    def intersect_line(self, other):
        # Using Cramer's rule
        det = self.a * other.b - other.a * self.b
        if abs(det) < EPSILON:
            # Lines are parallel or coincident
            if (abs(self.a * other.c - other.a * self.c) < EPSILON and
                abs(self.b * other.c - other.b * self.c) < EPSILON):
                return None  # Coincident (infinite points)
            return []  # Parallel (no points)

        x = (self.b * other.c - other.b * self.c) / det
        y = (other.a * self.c - self.a * other.c) / det
        return Point(x, y)

    def _get_two_points(self):
        if abs(self.b) > EPSILON:
            p1 = Point(0.0, -self.c / self.b)
            p2 = Point(1.0, -(self.c + self.a) / self.b)
        else:
            # Vertical line (b == 0)
            p1 = Point(-self.c / self.a, 0.0)
            p2 = Point(-self.c / self.a, 1.0)
        return p1, p2

    def translate(self, dx, dy):
        p1, p2 = self._get_two_points()
        p1.translate(dx, dy)
        p2.translate(dx, dy)
        self.__init__(p1=p1, p2=p2)

    def scale(self, factor, origin):
        p1, p2 = self._get_two_points()
        p1.scale(factor, origin)
        p2.scale(factor, origin)
        self.__init__(p1=p1, p2=p2)

    def rotate(self, angle_rad, origin):
        p1, p2 = self._get_two_points()
        p1.rotate(angle_rad, origin)
        p2.rotate(angle_rad, origin)
        self.__init__(p1=p1, p2=p2)

    def __repr__(self):
        return f"Line({self.a:.6f}x + {self.b:.6f}y + {self.c:.6f} = 0)"


class Circle:
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = float(radius)

    def intersect_line(self, line: Line):
        a, b = line.a, line.b
        c_prime = line.c + a * self.center.x + b * self.center.y
        r = self.radius

        denom = math.hypot(a, b)
        if denom < EPSILON:
            return []  

        dist = abs(c_prime) / denom

        if dist > r + EPSILON:
            return []
        
        norm_sq = a * a + b * b
        x0 = -a * c_prime / norm_sq
        y0 = -b * c_prime / norm_sq

        # Tangent check
        if abs(dist - r) < EPSILON:  
            return [Point(x0 + self.center.x, y0 + self.center.y)]

        # Two intersections
        # FIX: Clamp d to 0 to prevent domain error on tiny negative float noise
        d = max(0, r * r - (c_prime * c_prime) / norm_sq)
        
        mult = math.sqrt(d / norm_sq)

        ax = x0 + b * mult
        ay = y0 - a * mult
        bx = x0 - b * mult
        by = y0 + a * mult

        return [
            Point(ax + self.center.x, ay + self.center.y),
            Point(bx + self.center.x, by + self.center.y)
        ]

    def intersect_circle(self, other):
        d = self.center.distance_to(other.center)
        r1, r2 = self.radius, other.radius

        # Coincident circles
        if d < EPSILON and abs(r1 - r2) < EPSILON:
            return None

        # Separate (no intersection)
        if d > r1 + r2 + EPSILON:
            return []

        # Contained (one inside other)
        if d < abs(r1 - r2) - EPSILON:
            return []

        # Radical Axis Construction
        a = 2 * (other.center.x - self.center.x)
        b = 2 * (other.center.y - self.center.y)
        c = (self.center.x**2 - other.center.x**2 +
             self.center.y**2 - other.center.y**2 -
             self.radius**2 + other.radius**2)

        radical_axis = Line(a=a, b=b, c=c)
        
        # Intersection of the Radical Axis with the first circle
        return self.intersect_line(radical_axis)

    def translate(self, dx, dy):
        self.center.translate(dx, dy)

    def scale(self, factor, origin):
        self.center.scale(factor, origin)
        self.radius *= abs(factor)

    def rotate(self, angle_rad, origin):
        self.center.rotate(angle_rad, origin)

    def __repr__(self):
        return f"Circle(Center={self.center}, r={self.radius:.6f})"


class Triangle:
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.points = [p1, p2, p3]

    def translate(self, dx, dy):
        for p in self.points: p.translate(dx, dy)

    def scale(self, factor, origin):
        for p in self.points: p.scale(factor, origin)

    def rotate(self, angle_rad, origin):
        for p in self.points: p.rotate(angle_rad, origin)

    def __repr__(self):
        return f"Triangle({self.points[0]}, {self.points[1]}, {self.points[2]})"


# --- Verification Functions ---

def get_foot_of_perpendicular(line: Line, p: Point) -> Point:
    numerator = line.a * p.x + line.b * p.y + line.c
    denominator = line.a**2 + line.b**2
    if abs(denominator) < EPSILON:
        raise ValueError("Degenerate line in get_foot_of_perpendicular")
    x = p.x - line.a * (numerator / denominator)
    y = p.y - line.b * (numerator / denominator)
    return Point(x, y)


def verify_pythagorean_theorem(line: Line, external_point: Point):
    print("\n--- Pythagorean Verification ---")
    foot = get_foot_of_perpendicular(line, external_point)

    # Select arbitrary point on line (distinct from foot)
    if abs(line.b) > EPSILON:
        arbitrary_x = foot.x + 10.0
        arbitrary_y = (-line.c - line.a * arbitrary_x) / line.b
    else:
        arbitrary_y = foot.y + 10.0
        arbitrary_x = -line.c / line.a

    arbitrary_point = Point(arbitrary_x, arbitrary_y)

    a = external_point.distance_to(foot)          
    b = foot.distance_to(arbitrary_point)          
    c = external_point.distance_to(arbitrary_point)   

    print(f"External Point: {external_point}")
    print(f"Foot of Perp:   {foot}")
    print(f"Arbitrary Pt:   {arbitrary_point}")
    print(f"Side a (Alt):   {a:.6f}")
    print(f"Side b (Base):  {b:.6f}")
    print(f"Side c (Hyp):   {c:.6f}")

    lhs = a**2 + b**2
    rhs = c**2

    print(f"a² + b² = {lhs:.8f}")
    print(f"c²      = {rhs:.8f}")

    if abs(lhs - rhs) < 1e-5:
        print("VERIFIED: The relationship holds.")
    else:
        print("FAILED: Logic error in calculation.")


if __name__ == "__main__":
    p_origin = Point(0, 0)
    line1 = Line(p1=Point(0, 0), p2=Point(10, 10))  
    line2 = Line(p1=Point(0, 10), p2=Point(10, 0))  
    circ1 = Circle(Point(0, 0), 5)

    print("--- Intersections ---")
    ll = line1.intersect_line(line2)
    print(f"Line 1 & Line 2 Intersect: {ll}")

    # Line-Circle
    pts = circ1.intersect_line(line2)
    print(f"Line 2 & Circle 1 Intersect: {pts}")

    print("\n--- Transformations ---")
    t_point = Point(10, 0)
    print(f"Original: {t_point}")
    t_point.rotate(math.radians(90), p_origin)
    print(f"Rotated 90 deg: {t_point}")

    # Pythagorean Check
    test_line = Line(p1=Point(0, 0), p2=Point(10, 0))  # y = 0
    test_pt = Point(3, 4)
    verify_pythagorean_theorem(test_line, test_pt)

    # Circle-circle tests
    print("\n--- Circle-Circle Intersection ---")
    cA = Circle(Point(0, 0), 5)
    cB = Circle(Point(8, 0), 5)
    cc = cA.intersect_circle(cB)
    print(f"Circle A {cA}")
    print(f"Circle B {cB}")
    print(f"Intersection: {cc}")

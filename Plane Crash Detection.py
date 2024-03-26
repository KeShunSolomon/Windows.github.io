Python 3.10.4 (v3.10.4:9d38120e33, Mar 23 2022, 17:29:05) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
def main():
    class Plane:

        def __init__(self, name, x, y, vx, vy):
            self.name = name
            # plane represented by singular point
            self.x = x
            self.y = y
            # set x,y velocity and direction plane will move in
            self.vx = vx
            self.vy = vy

        def move(self):
            # planes move according to velocity
            self.x += self.vx  # move up 1 x value
            self.y += self.vy  # move up 1 y value

        def distance(self, other_plane):
            # calculate distance between two points
            dx = self.x - other_plane.x
            dy = self.y - other_plane.y
            return math.sqrt(dx ** 2 + dy ** 2)  # Euclidean distance formula

    ''' quadtree branches off into nodes '''

    class Node():

        def __init__(self, x, y, w, h, depth=0):
            # top left corner point
            self.x = x
            self.y = y
            # node dimensions
            self.width = w
            self.height = h
            # other attributes
            self.depth = depth
            self.planes = []  # planes inside node
            self.children = []  # node's children

        def split(self):  # divides node into 4 quadrants (child nodes)
            # determine midpoints of node
            child_w = self.width / 2  # child node width
            child_h = self.height / 2  # child node height

            # create child for each quadrant by calculating corner point
            nw = Node(self.x, self.y, child_w, child_h, self.depth + 1)
            ne = Node(self.x + child_w, self.y, child_w, child_h, self.depth + 1)
            sw = Node(self.x, self.y + child_h, child_w, child_h, self.depth + 1)
            se = Node(self.x + child_w, self.y + child_h, child_w, child_h, self.depth + 1)

            self.children = [nw, ne, sw, se]  # list of new child nodes

        def contains(self, plane):
            # checks if plane is within node boundaries
            return ((self.x <= plane.x <= (self.x + self.width)) and
                    (self.y <= plane.y <= (self.y + self.height)))

        # creates plane object, adds to planes list of current node
        def add_plane(self, plane):
            self.planes.append(plane)

    ''' quadtree that allows for plane insertion and collision detection '''

    class Quadtree():
        max_depth = 16  # tree limited to 16 segments
        max_planes = 1  # max planes in node before it subdivides

        def __init__(self, x, y, w, h):
            self.root = Node(x, y, w, h)  # set root node

        # insert plane object into quadtree
        def insert(self, plane, node=None):
            if node is None:
                node = self.root

            # if node has children, determine proper child node for plane
            if node.children:
                for child in node.children:
                    if child.contains(plane):
                        self.insert(plane, child)  # recursively insert into child node
                        return
            node.add_plane(plane)  # if no children, insert into current node

            # split node if necessary and move plane to child node
            if node.depth < self.max_depth and len(node.planes) > self.max_planes:
                if not node.children:  # if node is leaf
                    node.split()
                    # recursively add planes to proper child nodes
                    for p in node.planes:
                        for child in node.children:
                            if child.contains(p):
                                self.insert(p, child)
                    node.planes = []  # clear parent plane list
                else:
                    node.planes.remove(plane)  # remove plane from parent

    ''' initialize quadtree, plane objects, other variables'''
    quadtree = Quadtree(0, 0, 50, 50)  # quadtree with 50x50 dimensions

    # generate random x,y values for plane takeoff locations
    rx = random.randint(1, 50)
    ry = random.randint(1, 50)

    # create planes with initial positions
    plane1 = Plane("Plane 1", rx, 0, 0, 1)  # starts at (rx,0), moves up 1
    plane2 = Plane("Plane 2", 0, ry, 1, 0)  # starts at (0, ry), moves right 1

    # colliding planes for testing collision detector
    # plane1 = Plane("Plane 1", 25, 0, 0, 1)
    # plane2 = Plane("Plane 2", 0, 25, 1, 0)

    # min. distance for planes to be considered dangerously close
    danger_zone = 6  # 1 above status update frequency ensures warning

    redirector = random.randint(1, 3)

    i = 0
    max_i = 200  # max number of iterations (for debugging)

    ''' main loop, simulates plane quadtree traversal, checks for collisions'''
    while i < max_i:
        danger = False  # if planes are within danger zone

        # move plane
        plane1.move()
        plane2.move()

        # insert planes into quadtree
        quadtree.insert(plane1)
        quadtree.insert(plane2)

        # check if within danger zone
        if plane1.distance(plane2) <= danger_zone:
            # if planes collide, end loop
            if plane1.x == plane2.x and plane1.y == plane2.y:
                print("Simulation terminated: planes have collided. \n")
                break
            danger = True

        # print plane status every 5 iterations
        if i % 5 == 0:
            # warning message will print at least once before a collision
            if danger:
                print('WARNING: Planes are dangerously close!\n')
                if redirector == 2:
                    print('Redirecting!\n')
                    plane1.x += 5
            print(f"{plane1.name} Coordinates: {plane1.x},{plane1.y}")
            print(f"{plane2.name} Coordinates: {plane2.x},{plane2.y}\n")
            print("-------------------------------------------------\n")

        #  successful traversal message
        if not quadtree.root.contains(plane1) or not quadtree.root.contains(plane2):
            print('Simulation complete: Plane(s) safely traveled out of quadtree bounds.')
            break

        i += 1

        if i >= max_i:
            print('Error: max iterations reached.')
            break


if __name__ == '__main__':
    main()
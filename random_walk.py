from random import choice

class RandomWalk():
    """Class for generation accidental walking"""

    def __init__(self, num_points=5000):
        """Initializes attributes of walking"""
        self.num_points = num_points
        
        # All walkings starts from (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        # Defining direction and length of motion
            direction = choice([-1, 1])
            distance = choice([0, 1, 2, 3, 4])
            step = direction * distance

            return step

    def fill_walk(self):
        """Calculates all points of walking"""

        # Steps is generating till proper length
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            # Deviation from null's motion
            if x_step == 0 and y_step == 0:
                continue

            # Calculating next values of x and y
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

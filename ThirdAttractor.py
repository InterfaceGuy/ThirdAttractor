from manim import *
from manim_physics import *

class ThirdAttractor(Scene):
    def construct(self):
        # Create the ArrowVectorField
        charge1 = Charge(-10, 3.5 * LEFT + 1.5 * DOWN)
        charge2 = Charge(-10, 3.5 * RIGHT + 1.5 * DOWN)
        charge3 = Charge(-20, 1.5 * UP)
        field = ElectricField(charge1, charge2, charge3)

        # Define the callable function for the StreamLines
        def get_vector_at_point(point):
            vector = field.get_vector(point)
            return 5 * vector.get_vector()

        # Re-color the vectors
        def custom_color_scheme(vector):
            x, y = vector.get_vector()
            f1 = lambda x, y: np.exp(-((x - charge1.get_center()[0]) ** 2 + (y - charge1.get_center()[1]) ** 2))
            f2 = lambda x, y: -np.exp(-((x - charge2.get_center()[0]) ** 2 + (y - charge2.get_center()[1]) ** 2))
            z = f1(x, y) + f2(x, y)
            c1 = 100
            sigmoid = lambda x: 1 / (1 + np.exp(-c1 * x))
            return sigmoid(z)

        # Create the StreamLines and add it to the scene
        stream_lines = StreamLines(
            get_vector_at_point,
            #color_scheme=custom_color_scheme,
            stroke_width=3,
            max_anchors_per_line=3,
        )

        self.add(stream_lines)

        # Start the StreamLines animation
        stream_lines.start_animation(warm_up=True, flow_speed=2)
        self.wait(5)
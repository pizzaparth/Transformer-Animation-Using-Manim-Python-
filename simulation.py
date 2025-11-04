# Simulating a tranformer
from manim import *
config.frame_rate = 120
config.quality = "production_quality"
class Simulate(Scene):
    def construct(self):
        outer_core = Square(side_length=6, stroke_color=BLUE)
        inner_core = Square(side_length=4, stroke_color=BLUE)
        label_core = Text("This is the core of the transformer.")
        self.play(Create(outer_core),Create(inner_core), run_time=2)
        #self.play(Create(inner_core), run_time=0.5)
        self.play(Write(label_core), run_time=0.5)
        self.wait(1)
        self.play(RemoveTextLetterByLetter(label_core), run_time=0.5)
        #self.wait(1)


        # This is the primary part
        primary_loop_up = VGroup()
        primary_terminal_up = Line(start=[-6,2,0], end=[-2.8,2,0], color=YELLOW_D)
        primary_dot_up = Dot(point=[-6,2,0], radius=0.1)
        n_loops = 9  # number of loops
        spacing = 0.2  # space between loops

        for i in range(n_loops):
            loop = Circle(radius=0.5)
            loop.shift(i * spacing * UP)  # align loops vertically
            primary_loop_up.add(loop)
        primary_loop_up.shift(LEFT*2.5)
        self.play(Create(primary_loop_up), Create(primary_terminal_up), Create(primary_dot_up), run_time=0.1)
        
        primary_loop_down = VGroup()
        n_loops = 9  # number of loops
        spacing = 0.2  # space between loops
        primary_terminal_down = Line(start=[-2.8,-2,0], end=[-6,-2,0], color=YELLOW_D)
        primary_dot_down = Dot(point=[-6,-2,0], radius=0.1)

        for i in range(n_loops):
            loop = Circle(radius=0.5)
            loop.shift(i * spacing * DOWN)  # align loops vertically
            primary_loop_down.add(loop)
        primary_loop_down.shift(LEFT*2.5)
        self.play(Create(primary_loop_down), Create(primary_terminal_down), Create(primary_dot_down), run_time=0.1)


        # This is the secondary part
        seconday_loop_up = VGroup()
        n_loops = 9  # number of loops
        spacing = 0.2  # space between loops
        secondary_terminal_up = Line(start=[2.8,2,0], end=[6,2,0], color=YELLOW_D)
        secondary_dot_up = Dot(point=[6,2,0], radius=0.1)

        for i in range(n_loops):
            loop = Circle(radius=0.5)
            loop.shift(i * spacing * UP)  # align loops vertically
            seconday_loop_up.add(loop)
        seconday_loop_up.shift(RIGHT*2.5)
        self.play(Create(seconday_loop_up), Create(secondary_terminal_up), Create(secondary_dot_up), run_time=0.1)
        
        secondary_loop_down = VGroup()
        n_loops = 9  # number of loops
        spacing = 0.2  # space between loops
        secondary_terminal_down = Line(start=[6,-2,0], end=[2.8,-2,0], color=YELLOW_D)
        secondary_dot_down = Dot(point=[6,-2,0], radius=0.1)

        for i in range(n_loops):
            loop = Circle(radius=0.5)
            loop.shift(i * spacing * DOWN)  # align loops vertically
            secondary_loop_down.add(loop)
        secondary_loop_down.shift(RIGHT*2.5)
        self.play(Create(secondary_loop_down), Create(secondary_terminal_down), Create(secondary_dot_down), run_time=0.1)
        #self.wait(2)

        # Primary texts
        primary_text = Text("Primary windings.", font_size=16)
        primary_text.shift(LEFT*4.5)

        # Secondary texts
        secondary_text = Text("Secondary windings.", font_size=16)
        secondary_text.shift(RIGHT*4.5)
        self.play(Write(primary_text), Write(secondary_text), run_time=1)

        self.wait(5)

        # Primary dots
        primary_current_dot_up = Dot(point=[-6,2,0], radius=[0.1], color=PINK)
        anim1 = MoveAlongPath(primary_current_dot_up, primary_terminal_up, rate_functions=linear)
        
        primary_current_dot_down = Dot(point=[-2.8,-2,0], radius=[0.1], color=PINK)
        anim2 = MoveAlongPath(primary_current_dot_down, primary_terminal_down, rate_functions=linear)
        primary_current_text = Text("Primary Current.", font_size=12)
        primary_current_text.shift(LEFT*4.5)
        primary_current_text.shift(UP*2.2)

        # Secondary dots
        secondary_current_dot_up = Dot(point=[6,2,0], radius=[0.1], color=LIGHT_BROWN)
        anim3 = MoveAlongPath(secondary_current_dot_up, secondary_terminal_up, rate_functions=linear)
        
        secondary_current_dot_down = Dot(point=[2.8,-2,0], radius=[0.1], color=LIGHT_BROWN)
        anim4 = MoveAlongPath(secondary_current_dot_down, secondary_terminal_down, rate_functions=linear)
        secondary_current_text = Text("Secondary Current.", font_size=12)
        secondary_current_text.shift(RIGHT*4.5)
        secondary_current_text.shift(UP*2.2)

        self.play(anim1, anim2, anim3, anim4, run_time=2)

        # FLux Path
        square_basic = Square(side_length=5, stroke_color=WHITE)
        flux_path = DashedVMobject(square_basic)  # Make the square dashed
        #self.wait(2)
        flux_path.set_stroke(opacity=0.3)

        # Field lines
        l1 = Ellipse(width=4.5, height=5, color=GREEN)
        l2 = Ellipse(width=4.6, height=6, color=GREEN)
        l3 = Ellipse(width=4.7, height=7, color=GREEN)
        l4 = Ellipse(width=4.8, height=8, color=GREEN)
        l5 = Ellipse(width=4.9, height=9, color=GREEN)
        
        a1 = Ellipse(width=0.3, height=2, color=GREEN)
        a1.shift(LEFT*3)
        a2 = Ellipse(width=0.6, height=3, color=GREEN)
        a2.shift(LEFT*3)
        a3 = Ellipse(width=0.9, height=4, color=GREEN)
        a3.shift(LEFT*3)

        b1 = Ellipse(width=0.3, height=2, color=GREEN)
        b1.shift(RIGHT*3)
        b2 = Ellipse(width=0.6, height=3, color=GREEN)
        b2.shift(RIGHT*3)
        b3 = Ellipse(width=0.9, height=4, color=GREEN)
        b3.shift(RIGHT*3)

        self.play(Create(primary_current_dot_up), Create(primary_current_dot_down), Create(primary_current_text), Create(secondary_current_text), Create(secondary_current_dot_up), Create(secondary_current_dot_down), Create(flux_path),run_time=0.1)

        self.play(Create(l1), run_time=0.1)
        self.play(Create(l2), run_time=0.1)
        self.play(Create(l3), run_time=0.1)
        self.play(Create(l4), run_time=0.1)
        self.play(Create(l5), run_time=0.1)

        self.play(Create(a1), Create(a2), Create(a3),Create(b1), Create(b2), Create(b3), run_time=0.1)
        

        duration = 20
        while duration > 0:
            self.play(anim1, anim2, anim3, anim4, run_time=1)
            duration = duration - 1

        
        self.wait(10)
            duration = duration - 1

        
        self.wait(10)

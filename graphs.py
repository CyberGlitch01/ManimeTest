from manim import *
import numpy as np

class Intro(Scene):
    def construct(self):
        animatedBy = Text("Common Graphs", font_size=24)
        animatedBy.to_corner(DR)
        animatedBy.set_opacity(0.5)
        self.add(animatedBy)
        text = Text("Innovative Creations of software technology", font_size=24)
        self.play(Write(text))
        self.wait(1)

        self.play(
            text.animate
            .scale(10)
            .fade(1),
            run_time=2
        )
        self.wait(1)

class Graphs(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-10, 10, 1],
            y_range=[-1000, 1000, 200],
            tips=True
        )
        self.play(Create(axes), run_time=4)
        square = axes.plot(
            lambda x : x ** 2,
            x_range=[-10, 10, 1],
            color=BLUE
        )
        square_label = axes.get_graph_label(square, label="x^2")
        self.play(Create(square_label), runt_time=0.5)
        self.play(Create(square), run_time=4)
        self.wait(1)

        cubic = axes.plot(
            lambda x : x ** 3,
            x_range=[-10, 10, 1],
            color=YELLOW
        )
        cube_label = axes.get_graph_label(cubic, label="x^3")
        self.play(Create(cube_label), runt_time=0.5)
        self.play(Create(cubic), run_time=4)
        self.wait(1)
        sin = axes.plot(
            lambda x : 200 * (np.sin(x)),
            x_range=[-10, 10, 0.5],
            color=PINK
        )
        sin_label = axes.get_graph_label(sin, label="200.sin(x)")
        self.play(Create(sin_label), runt_time=0.5)
        self.play(Create(sin), run_time=4)
        self.wait(1)
        cos = axes.plot(
            lambda x : 200 * (np.cos(x)),
            x_range=[-10, 10, 0.5],
            color=TEAL
        )
        cos_label = axes.get_graph_label(cos, label="200.cos(x)", x_val=-10)
        self.play(Create(cos_label), runt_time=0.5)
        self.play(Create(cos), run_time=4)
        self.wait(1)

        exponential = axes.plot(
            lambda x : 2.71828183 ** x,
            x_range=[-10, 10, 0.5],
            color=RED
        )
        exponential_label = axes.get_graph_label(exponential, label="e^x")
        self.play(Create(exponential_label), runt_time=0.5)
        self.play(Create(exponential), run_time=4)
        self.wait(1)

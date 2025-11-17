from manim import *
import numpy as np

class Intro(Scene):
    def construct(self):
        animatedBy = Text("Mathematics of a circle", font_size=24)
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

class CircleScene(Scene):
    def construct(self):
        axes = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-100, 100, 1],
        ).scale(0.6)
        self.add(axes)

        h_val = ValueTracker(0)
        k_val = ValueTracker(0)
        r_val = ValueTracker(2)

        def get_center():
            return axes.c2p(h_val.get_value(), k_val.get_value())

        def get_radius():
            return r_val.get_value() * axes.x_axis.unit_size

        circle = ParametricFunction(
            lambda t: get_center() + np.array([
                get_radius() * np.cos(t),
                get_radius() * np.sin(t),
                0
            ]),
            t_range=[0, TAU],
            color=WHITE
        ).scale(0.6)

        circle.add_updater(
            lambda mob: mob.become(
                ParametricFunction(
                    lambda t: get_center() + np.array([
                        get_radius() * np.cos(t),
                        get_radius() * np.sin(t),
                        0
                    ]),
                    t_range=[0, TAU],
                    color=WHITE
                ).scale(0.6)
            )
        )

        self.play(Create(circle), run_time=3)

        equation = MathTex(
            f"(x + ({-h_val.get_value()}))^2 + (y + ({-k_val.get_value()}))^2 = 2^2",
            font_size=48
        )
        equation.to_corner(UR)

        def eq_updater(mob):
            new_eq = MathTex(
                f"(x + ({-h_val.get_value():.1f}))^2 + (y + ({-k_val.get_value():.1f}))^2 = {r_val.get_value():.1f}^2",
                font_size=48
            )
            new_eq.to_corner(UR)
            mob.become(new_eq)

        equation.add_updater(eq_updater)
        self.play(Write(equation), run_time=1)
        self.add(equation)

        self.wait(1)
        self.play(h_val.animate.set_value(4), run_time=2)
        self.wait(0.5)
        self.play(k_val.animate.set_value(2), run_time=2)
        self.wait(0.5)
        self.play(r_val.animate.set_value(4), run_time=2)
        self.wait(0.5)
        self.play(k_val.animate.set_value(-2), run_time=2)
        self.wait(0.5)
        self.play(
            h_val.animate.set_value(-3),
            k_val.animate.set_value(2),
            run_time=2
        )
        self.wait(0.5)
        self.play(
            h_val.animate.set_value(-3),
            k_val.animate.set_value(-3),
            r_val.animate.set_value(3),
            run_time=3
        )
        self.wait(0.5)
        self.play(
            h_val.animate.set_value(0),
            k_val.animate.set_value(0),
            r_val.animate.set_value(2),
            run_time=3
        )
        self.wait(2)

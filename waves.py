from manim import *
import numpy as np

class Intro(Scene):
    def construct(self):
        MathTex = MathTex("Wave in motion", font_size=24)
        self.play(Write(MathTex))
        self.wait(1)

        self.play(
            MathTex.animate.fade(1),
            run_time=2
        )
        self.wait(1)


class WaveScene(Scene):
    @staticmethod
    def sinWave(t, velocity, wavelength, x, fi):
        k = 2 * PI / wavelength
        return np.sin((2 * PI * velocity / wavelength * t) + (k * x) + fi)

    def construct(self):
        axes = Axes(
            x_range=[-2, 10, 1],
            y_range=[-5, 5, 1]
        )
        self.add(axes)
        self.play(Create(axes), run_time=0.5)

        wavelength = ValueTracker(0.5)
        time = ValueTracker(0.0)
        fi = ValueTracker(0.0)
        velocity = ValueTracker(15.0)

        def getWaveParamCurve() -> ParametricFunction:
            wave = ParametricFunction(
                lambda x : np.array(
                    axes.c2p(
                        x, 
                        WaveScene.sinWave(time.get_value(), velocity.get_value(), wavelength.get_value(), x, fi.get_value()),
                        0
                    )
                ),
                t_range=[0, 8],
                color=GREEN
            )
            return wave
        
        wave = getWaveParamCurve()
        source = Dot(wave.get_start())

        infoMathTexSize = 32
        info = VGroup(
            MathTex(
                rf"Angular frequency (\omega) : {(2 * PI * velocity.get_value() / wavelength.get_value()):.2f} rad/s",
                font_size=infoMathTexSize,
                color=YELLOW
            ),
            MathTex(
                rf"Wavelength (\lambda) : {wavelength.get_value():.2f} m",
                font_size=infoMathTexSize,
                color=RED
            ),
            MathTex(
                rf"Velocity (v) : {velocity.get_value():.2f} m/s",
                font_size=infoMathTexSize,
                color=BLUE
            ),
            MathTex(
                rf"Time (t) : {(time.get_value()):.2f} s",
                font_size=infoMathTexSize,
                color=TEAL
            )
        )
        info.arrange(DOWN, aligned_edge=LEFT)
        info.to_corner(DL)
        self.add(info)
        self.play(Write(info))
        
        def updateInfo(self):
            newInfo = VGroup(
                MathTex(
                    rf"Angular frequency (\omega) : {(2 * PI * velocity.get_value() / wavelength.get_value()):.2f} rad/s",
                    font_size=infoMathTexSize,
                    color=YELLOW
                ),
                MathTex(
                rf"Wavelength (\lambda) : {wavelength.get_value():.2f} m",
                font_size=infoMathTexSize,
                color=RED
                ),
                MathTex(
                rf"Velocity (v) : {velocity.get_value():.2f} m/s",
                font_size=infoMathTexSize,
                color=BLUE
                ),
                MathTex(
                rf"Time (t) : {(time.get_value()):.2f} s",
                font_size=infoMathTexSize,
                color=TEAL
                )
            )
            newInfo.arrange(DOWN, aligned_edge=LEFT)
            newInfo.to_corner(DL)
            info.become(newInfo)

        def updateWave(self):
            newWave = getWaveParamCurve()
            wave.become(newWave)
                                            
        def updateSource(self):
            source.become(Dot(wave.get_start()))
        
        source.add_updater(updateSource)
        wave.add_updater(updateWave)
        info.add_updater(updateInfo)

        self.add(wave, source)

        self.play(time.animate.set_value(5), run_time=5)
        self.wait(1)
        self.play(wavelength.animate.set_value(1), run_time=5)
        self.wait(1)
        self.play(velocity.animate.set_value(5), run_time=5)
        self.wait(1)
        self.play(time.animate.set_value(10), run_time=5)
        self.wait(1)

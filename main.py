from manim import *


class ParafieldStudios(Scene):
    def construct(self):
        text = Text("PARAFIELD \n STUDIOS", font="Segoe UI", weight="BOLD")
        logo = SVGMobject("parafield.svg")
        self.play(FadeIn(logo), run_time=1.5)
        self.play(
            AnimationGroup(
                logo.animate.next_to(text, LEFT), Write(text), lag_ratio=0.8
            ),
            run_time=3,
        )
        self.wait(2)
        self.play(FadeOut(logo, text), run_time=1.5)

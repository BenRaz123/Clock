from manim import *
import datetime
from random import randint

rawTime = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
print(rawTime)

def switchToNormalHours(a:str) -> str:
    splitted = a.split(":")
    hours = splitted[0]
    hours = int(hours)
    res = a
    if int(hours) > 12:
        hours -= 12
        res = f"{hours}:{splitted[1]}:{splitted[2]} PM"
    else:
        res+=" AM"

    return res

class Clock(Scene):
    def construct(self):
        backgroundSquare = Rectangle(width=100, height=70, fill_opacity=1, fill_color=DARKER_GRAY)
        self.add(backgroundSquare)

        obj_1 = VGroup(*[Square(fill_opacity=1, stroke_opacity=0, color="#1d4") for _ in range(3)])

        obj_1[1].next_to(obj_1[0], DOWN, buff=-0.01)
        obj_1[2].next_to(obj_1[0], LEFT, buff=-0.01)

        obj_1.rotate(PI / -4).center()
        obj_2 = obj_1.copy().set(fill_color=LIGHTER_GRAY).next_to(obj_1, LEFT, buff=-0.5)

        text = Text("Coding Club", font="Share Tech Mono", color=WHITE, weight=BOOK).scale(4).next_to(obj_1,
                                                                                                            RIGHT,
                                                                                                            buff=1.5)
        logo = VGroup(obj_2, obj_1, text).center().scale(0.35)

        self.wait()

        self.play(
            LaggedStart(
                LaggedStart(
                    FadeIn(obj_1, shift=RIGHT, rate_func=rate_functions.ease_in_out_quad),
                    FadeIn(obj_2, shift=RIGHT * 1.25, rate_func=rate_functions.ease_in_out_quad),
                    lag_ratio=0.3
                ),
                FadeIn(text, shift=DOWN * 0.1),
                lag_ratio=0.3
            )
        )

        self.wait()

        self.play(logo.animate.to_corner(UP, buff=0).scale(0.5))



        counter = 0
        textColor = "#1d4"
        normalColor = WHITE
        bgColor = DARKER_GRAY
        while True:
            """
            if counter == 100:
                counter = 0
                normalColor = BLACK if normalColor == WHITE else WHITE
                textColor = DARKER_GRAY if textColor == "#1d4" else "#1d4"
                bgColor = "#1d4" if bgColor == DARKER_GRAY else DARKER_GRAY
                backgroundSquare.set(fill_color=bgColor)

            counter += 1
            """
            time = switchToNormalHours(datetime.datetime.now().strftime("%H:%M:%S.%f")[:-5])

            timeDisplay = Text(time, font="Share Tech Mono", color=textColor, weight=BOLD).scale(2)

            self.add(timeDisplay)
            self.wait(0.01)
            self.remove(timeDisplay)

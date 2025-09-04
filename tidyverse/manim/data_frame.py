from manim import *

class DataFrame(MobjectTable):
    def __init__(self, table, **kwargs):
        super().__init__(table, **kwargs)

        self.bg_rectangles = dict()

    def add_bg_rectangle(self, pos, color = None, **kwargs):
        rect = self.get_highlighted_cell(pos, color, fill_opacity=1, **kwargs)
        rect.set_z_index(-1)
        self.add(rect)
        self.bg_rectangles[pos] = rect
        return rect

    def get_cell_copy(self, pos):
        group = VGroup(
            self.get_cell(pos, color=WHITE).copy(),
            self.get_entries(pos).copy(),
        )

        if pos in self.bg_rectangles: group.add(self.bg_rectangles[pos].copy())

        return group
    
    def animate_cell_movement(self, pos, other, other_pos, 
                              transform_entry=False, move_bg=True, fade_bg=False, rate_func=rate_functions.linear, **kwargs):
        if transform_entry:
            entry_animation=Transform(self.get_entries(pos).copy(), other.get_entries(other_pos))
        else:
            entry_animation=self.get_entries(pos).copy().animate.move_to(other.get_entries(other_pos))
        
        animation_group = [
            Transform(self.get_cell(pos, color=WHITE).copy(), other.get_cell(other_pos, color=WHITE)),
            entry_animation
        ]

        if pos in self.bg_rectangles and move_bg: 
            opacity=0 if fade_bg else 1
            animation_group.append(
                self.bg_rectangles[pos].copy().animate.scale_to_fit_width(other.get_cell(other_pos).width).set_opacity(opacity).move_to(other.get_entries(other_pos))
            )
            # print("hi1", flush=True)
            # rect = self.bg_rectangles[pos].copy()
            # print("hi2", flush=True)
            # color = self.bg_rectangles[pos].get_fill_color()
            # print(color, flush=True)
            # new_rect = other.get_highlighted_cell(other_pos, color = color)
            # print("hi3", flush=True)
            # animation_group.append(
            #     Transform(rect, new_rect)
            # )
            # print("hi4", flush=True)

        
        return AnimationGroup(*animation_group, rate_func=rate_func, **kwargs)


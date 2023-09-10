from re import S
from manim import *

class BubbleSort(Scene):
    """
    Generate with:
    manim -ql --flush_cache bubble_sort.py BubbleSort
    """
    def construct(self):
        # The list of numbers we want to sort in ascending order.
        list = [7, 4, 5, 6, 1, 2, 3]

        # Create a group of squares and a group of numbers.
        g_cells, g_nums = self.create_cells_and_numbers(list)

        # Create the arrows
        a1g, a2g = self.create_arrows(g_cells)

        outer_loop = Text("outer loop - n:", font="Monospace").scale(0.5).to_edge(UL)
        inner_loop = (
            Text("inner loop - i:", font="Monospace")
            .scale(0.5)
            .next_to(outer_loop, DOWN)
        )
        indices = self.create_and_place_indices(g_cells)
        n_value = Integer(len(list)).scale(0.8).next_to(outer_loop, RIGHT)
        i_value = Integer(0).scale(0.8).next_to(inner_loop, RIGHT)

        # Add all groups to the scene.
        self.add(g_cells, g_nums, a1g, a2g, outer_loop, n_value, inner_loop, i_value, indices)

        # 'last' is the index of the last item (Lists in Python are zero-based)
        last = len(list) - 1
        # The outer loop needs as many iterations as the amount of list items.
        n = len(list) - 1
        while n >= 0:
            self.play(
                # Update animation of outer loop counter.
                Flash(n_value),
                n_value.animate.set_value(n),
            )

            # Reset the inner counter.
            i = 0
            while i < last:
                self.play(
                    # Slide the arrows under the list items being compared.
                    a1g.animate.next_to(g_cells[i], DOWN, buff=0.5),
                    a2g.animate.next_to(g_cells[i + 1], DOWN, buff=0.5),
                    # Update animation of inner loop counter.
                    Flash(i_value),
                    i_value.animate.set_value(i)
                )
                # Change the background color of the squares to yellow.
                self.play(
                    g_cells[i].animate.set_fill(color=YELLOW, opacity=0.3),
                    g_cells[i + 1].animate.set_fill(color=YELLOW, opacity=0.3),
                )

                a = g_nums[i]
                b = g_nums[i + 1]
                # If the numbers are not in the right order (ascending)
                if a.get_value() > b.get_value():
                    # Change the background color of the squares to red.
                    self.play(
                        g_cells[i].animate.set_fill(color=RED, opacity=0.3),
                        g_cells[i + 1].animate.set_fill(color=RED, opacity=0.3),
                    )
                    # Store the center of the Mobject to the left.
                    tmp = a.get_center()
                    # Swap the positions of the Mobjects.
                    self.play(
                        a.animate.move_to(b.get_center()),
                        b.animate.move_to(tmp),
                    )
                    # Swap the Mobjects in the VGroup.
                    g_nums[i], g_nums[i + 1] = g_nums[i + 1], g_nums[i]
                else:
                    # Change the background color of the squares to green.
                    self.play(
                        g_cells[i].animate.set_fill(color=GREEN, opacity=0.3),
                        g_cells[i + 1].animate.set_fill(color=GREEN, opacity=0.3),
                    )

                # Remove the red/green background.
                self.play(
                    g_cells[i].animate.set_fill(opacity=0),
                    g_cells[i + 1].animate.set_fill(opacity=0),
                )
                # Increment the inner counter.
                i += 1
            # Decrement the remaining amount of outer loop passes.
            n -= 1

    def create_and_place_indices(self, cells):
        indices = VGroup()

        for i, cell in enumerate(cells):
            n = Text(str(i), font='Monospace', fill_opacity=0.5).scale(0.4).next_to(cell, DOWN, buff=0.125).shift(LEFT * 0.25)
            indices.add(n)
        return indices

    def create_cells_and_numbers(self, list):
        # Create a group of squares and a group of numbers.
        g_cells = VGroup()
        g_nums = VGroup()

        # Traverse the list of numbers.
        for i in list:
            # Create a cell (Square Mobject).
            cell = Square(side_length=1, color=WHITE)

            # Make an Integer Mobject out of each number in the original list.
            num = Integer(i, color=WHITE)

            # For all the cells, other than the first one.
            if len(g_cells) > 0:
                # Position the cell right next to the previous square.
                cell.next_to(g_cells[-1], RIGHT, buff=0)

            # Move the integer Mobject to the center of the cell.
            num.move_to(cell.get_center())
            # Add the square to the list of cells.
            g_cells.add(cell)
            # Add the number to the list of numbers.
            g_nums.add(num)

        # Move the group of cells to the center.
        g_cells.move_to(ORIGIN)
        # Move the group of numbers to the center.
        g_nums.move_to(ORIGIN)

        return g_cells, g_nums

    def create_arrows(self, g_cells):
        # Create arrow 'i'.
        arrow = Arrow(
            start=DOWN,
            end=UP,
        ).scale(0.5, scale_tips=True)
        # Create a label for the arrow.
        label = Text("i", color=WHITE).next_to(arrow, DOWN, buff=0).scale(0.6)
        # Group them both.
        a1g = VGroup(arrow, label).next_to(g_cells[0], DOWN, buff=0.5)

        # Create arrow 'i+1'.
        arrow2 = arrow.copy()
        a2g = VGroup(
            arrow2, Text("i+1", color=WHITE).next_to(arrow2, DOWN, buff=0).scale(0.6)
        ).next_to(g_cells[1], DOWN, buff=0.5)

        return a1g, a2g


class BubbleSort2(Scene):
    """
    Illustrate inefficiency of first implementation.

    Generate with:
    manim -ql --flush_cache bubble_sort.py BubbleSort2
    """
    def construct(self):
        # The list of numbers we want to sort in ascending order.
        list = [7, 4, 5, 6, 1, 2, 3]

        # Create a group of squares and a group of numbers.
        g_cells, g_nums = self.create_cells_and_numbers(list)

        # Create the arrows
        a1g, a2g = self.create_arrows(g_cells)

        # Create legends for the outer and inner loops.
        outer_loop = Text("outer loop - n:", font="Monospace").scale(0.5).to_edge(UL)
        inner_loop = (
            Text("inner loop - i:", font="Monospace")
            .scale(0.5)
            .next_to(outer_loop, DOWN)
        )
        indices = self.create_and_place_indices(g_cells)
        n_value = Integer(len(list)).scale(0.8).next_to(outer_loop, RIGHT)
        i_value = Integer(0).scale(0.8).next_to(inner_loop, RIGHT)

        # Add all groups to the scene.
        self.add(g_cells, g_nums, a1g, a2g, outer_loop, n_value, inner_loop, i_value, indices)

        # 'last' is the index of the last item (Lists in Python are zero-based)
        last = len(list) - 1
        # The outer loop needs as many iterations as the amount of list items.
        n = len(list) - 1
        while n >= 0:
            self.play(
                # Update animation of outer loop counter.
                Flash(n_value),
                n_value.animate.set_value(n),
            )

            # Reset the inner counter.
            i = 0
            while i < last:
                self.play(
                    # Slide the arrows under the list items being compared.
                    a1g.animate.next_to(g_cells[i], DOWN, buff=0.5),
                    a2g.animate.next_to(g_cells[i + 1], DOWN, buff=0.5),
                    # Update animation of inner loop counter.
                    Flash(i_value),
                    i_value.animate.set_value(i)
                )
                # Change the background color of the squares to yellow.
                self.play(
                    g_cells[i].animate.set_fill(color=YELLOW, opacity=0.3),
                    g_cells[i + 1].animate.set_fill(color=YELLOW, opacity=0.3),
                )

                a = g_nums[i]
                b = g_nums[i + 1]
                # If the numbers are not in the right order (ascending)
                if a.get_value() > b.get_value():
                    # Change the background color of the squares to red.
                    self.play(
                        g_cells[i].animate.set_fill(color=RED, opacity=0.3),
                        g_cells[i + 1].animate.set_fill(color=RED, opacity=0.3),
                    )
                    # Store the center of the Mobject to the left.
                    tmp = a.get_center()
                    # Swap the positions of the Mobjects.
                    self.play(
                        a.animate.move_to(b.get_center()),
                        b.animate.move_to(tmp),
                    )
                    # Swap the Mobjects in the VGroup.
                    g_nums[i], g_nums[i + 1] = g_nums[i + 1], g_nums[i]
                else:
                    # Change the background color of the squares to green.
                    self.play(
                        g_cells[i].animate.set_fill(color=GREEN, opacity=0.3),
                        g_cells[i + 1].animate.set_fill(color=GREEN, opacity=0.3),
                    )

                # Remove the red/green background.
                self.play(
                    g_cells[i].animate.set_fill(opacity=0),
                    g_cells[i + 1].animate.set_fill(opacity=0),
                )

                # BRACES: If the second item being compared is the last one.
                if i + 1 >= n:
                    # If 'n' is at the last index.
                    if n == len(list) - 1:
                        sorted_brace = False

                    new_sorted_brace = self.create_sorted_brace(g_cells, n)
                    # If there's some item already sorted,
                    # transform the old brace into the new one.
                    if sorted_brace:
                        self.play(FadeTransform(sorted_brace, new_sorted_brace))
                    else:
                        self.play(FadeIn(new_sorted_brace))
                    # A small switcharoo for the next outer loop pass.
                    sorted_brace = new_sorted_brace

                # Increment the inner counter.
                i += 1
            # Decrement the remaining amount of outer loop passes.
            n -= 1

    def create_and_place_indices(self, cells):
        indices = VGroup()

        for i, cell in enumerate(cells):
            n = Text(str(i), font='Monospace', fill_opacity=0.5).scale(0.4).next_to(cell, DOWN, buff=0.125).shift(LEFT * 0.25)
            indices.add(n)
        return indices

    def create_cells_and_numbers(self, list):
        # Create a group of squares and a group of numbers.
        g_cells = VGroup()
        g_nums = VGroup()

        # Traverse the list of numbers.
        for i in list:
            # Create a cell (Square Mobject).
            cell = Square(side_length=1, color=WHITE)

            # Make an Integer Mobject out of each number in the original list.
            num = Integer(i, color=WHITE)

            # For all the cells, other than the first one.
            if len(g_cells) > 0:
                # Position the cell right next to the previous square.
                cell.next_to(g_cells[-1], RIGHT, buff=0)

            # Move the integer Mobject to the center of the cell.
            num.move_to(cell.get_center())
            # Add the square to the list of cells.
            g_cells.add(cell)
            # Add the number to the list of numbers.
            g_nums.add(num)

        # Move the group of cells to the center.
        g_cells.move_to(ORIGIN)
        # Move the group of numbers to the center.
        g_nums.move_to(ORIGIN)

        return g_cells, g_nums

    def create_arrows(self, g_cells):
        # Create arrow 'i'.
        arrow = Arrow(
            start=DOWN,
            end=UP,
        ).scale(0.5, scale_tips=True)
        # Create a label for the arrow.
        label = Text("i", color=WHITE).next_to(arrow, DOWN, buff=0).scale(0.6)
        # Group them both.
        a1g = VGroup(arrow, label).next_to(g_cells[0], DOWN, buff=0.5)

        # Create arrow 'i+1'.
        arrow2 = arrow.copy()
        a2g = VGroup(
            arrow2, Text("i+1", color=WHITE).next_to(arrow2, DOWN, buff=0).scale(0.6)
        ).next_to(g_cells[1], DOWN, buff=0.5)

        return a1g, a2g

    def create_sorted_brace(self, g_cells, n):
        # Store last cell in a variable.
        last_cell = g_cells[len(g_cells) - 1]

        # Store right edge in a variable (right_edge = last_cell.get_right()).
        right_edge = g_cells.get_critical_point(RIGHT)

        # Create a new brace (bigger after 1st n pass) and place it.
        temp_group = VGroup(g_cells[n], last_cell)

        new_brace_left = temp_group.get_left()
        new_brace = BraceBetweenPoints(new_brace_left, right_edge, UP)
        new_brace.next_to(temp_group, UP, buff=0.125)

        # Create a label and place next to the new brace.
        label = Text("Sorted", color=WHITE).scale(0.5)
        label.next_to(new_brace, UP, buff=0.125)

        # Group the brace and the label.
        return VGroup(new_brace, label)


class BubbleSort3(Scene):
    """
    Generate with:
    manim -ql --flush_cache bubble_sort.py BubbleSort3

    Add 1st optimization (shrinking list after each outer loop full-pass)
    """
    def construct(self):
        # The list of numbers we want to sort in ascending order.
        list = [7, 4, 5, 6, 1, 2, 3]
        
        # Create a group of squares and a group of numbers.
        g_cells, g_nums = self.create_cells_and_numbers(list)

        # Create the arrows
        a1g, a2g = self.create_arrows(g_cells)

        # Create legends for the outer and inner loops.
        outer_loop = Text("outer loop - n:", font="Monospace").scale(0.5).to_edge(UL)
        inner_loop = (
            Text("inner loop - i:", font="Monospace")
            .scale(0.5)
            .next_to(outer_loop, DOWN)
        )
        indices = self.create_and_place_indices(g_cells)
        n_value = Integer(len(list) - 1).scale(0.8).next_to(outer_loop, RIGHT)
        i_value = Integer(0).scale(0.8).next_to(inner_loop, RIGHT)

        # Create 'n' arrow.
        n_arrow = self.create_n_arrow(g_cells)

        # Add all groups to the scene.
        self.add(
            g_cells,
            g_nums,
            a1g,
            a2g,
            outer_loop,
            n_value,
            inner_loop,
            i_value,
            indices,
            n_arrow
        )

        n = len(g_nums) - 1
        while n > 0:
            # Update animation of outer loop counter.
            self.play(
                Flash(n_value),
                n_value.animate.set_value(n),
                # Slide the end arrow under the last list item.
                n_arrow.animate.next_to(g_cells[n], UP, buff=0.125),
            )

            i = 0   # Reset the inner counter.
            while i < n:
                self.play(
                    # Slide the arrows under the list items being compared.
                    a1g.animate.next_to(g_cells[i], DOWN, buff=0.5),
                    a2g.animate.next_to(g_cells[i + 1], DOWN, buff=0.5),
                    # Update animation of inner loop counter.
                    Flash(i_value),
                    i_value.animate.set_value(i)
                )
                # Change the background color of the squares to yellow.
                self.play(
                    g_cells[i].animate.set_fill(color=YELLOW, opacity=0.3),
                    g_cells[i + 1].animate.set_fill(color=YELLOW, opacity=0.3),
                )

                a = g_nums[i]
                b = g_nums[i + 1]
                # If the numbers are not in the right order (ascending)
                if a.get_value() > b.get_value():
                    # Change the background color of the squares to red.
                    self.play(
                        g_cells[i].animate.set_fill(color=RED, opacity=0.3),
                        g_cells[i + 1].animate.set_fill(color=RED, opacity=0.3),
                    )
                    # Store the center of the Mobject to the left.
                    tmp = a.get_center()
                    # Swap the positions of the Mobjects.
                    self.play(
                        a.animate.move_to(b.get_center()),
                        b.animate.move_to(tmp),
                    )
                    # Swap the Mobjects in the VGroup.
                    g_nums[i], g_nums[i + 1] = g_nums[i + 1], g_nums[i]
                else:
                    # Change the background color of the squares to green.
                    self.play(
                        g_cells[i].animate.set_fill(color=GREEN, opacity=0.3),
                        g_cells[i + 1].animate.set_fill(color=GREEN, opacity=0.3),
                    )

                # Remove the red/green background.
                self.play(
                    g_cells[i].animate.set_fill(opacity=0),
                    g_cells[i + 1].animate.set_fill(opacity=0),
                )
                # Increment the inner counter.
                i += 1
            # Turn the last cell grey.
            self.play(
                g_cells[n].animate.set_color(GRAY),
                g_nums[n].animate.set_color(GRAY),
            )
            # Decrement the remaining amount of outer loop passes.
            n -= 1
    
    def create_and_place_indices(self, cells):
        indices = VGroup()

        for i, cell in enumerate(cells):
            n = Text(str(i), font='Monospace', fill_opacity=0.5).scale(0.4).next_to(cell, DOWN, buff=0.125).shift(LEFT * 0.25)
            indices.add(n)
        return indices

    def create_cells_and_numbers(self, list):
        # Create a group of squares and a group of numbers.
        g_cells = VGroup()
        g_nums = VGroup()

        # Traverse the list of numbers.
        for i in list:
            # Create a cell (Square Mobject).
            cell = Square(side_length=1, color=WHITE)

            # Make an Integer Mobject out of each number in the original list.
            num = Integer(i, color=WHITE)

            # For all the cells, other than the first one.
            if len(g_cells) > 0:
                # Position the cell right next to the previous square.
                cell.next_to(g_cells[-1], RIGHT, buff=0)

            # Move the integer Mobject to the center of the cell.
            num.move_to(cell.get_center())
            # Add the square to the list of cells.
            g_cells.add(cell)
            # Add the number to the list of numbers.
            g_nums.add(num)

        # Move the group of cells to the center.
        g_cells.move_to(ORIGIN)
        # Move the group of numbers to the center.
        g_nums.move_to(ORIGIN)

        return g_cells, g_nums

    def create_arrows(self, g_cells):
        # Create arrow 'i'.
        arrow = Arrow(
            start=DOWN,
            end=UP,
        ).scale(0.5, scale_tips=True)
        # Create a label for the arrow.
        label = Text("i", color=WHITE).next_to(arrow, DOWN, buff=0).scale(0.6)
        # Group them both.
        a1g = VGroup(arrow, label).next_to(g_cells[0], DOWN, buff=0.5)

        # Create arrow 'i+1'.
        arrow2 = arrow.copy()
        a2g = VGroup(
            arrow2, Text("i+1", color=WHITE).next_to(arrow2, DOWN, buff=0).scale(0.6)
        ).next_to(g_cells[1], DOWN, buff=0.5)

        return a1g, a2g
    
    def create_n_arrow(self, cells):
        # Create an arrow
        arrow = Arrow(
            start=UP,
            end=DOWN,
        ).scale(0.5, scale_tips=True)

        # Create a label for the arrow.
        label = Text("n", color=WHITE).next_to(arrow, UP, buff=0).scale(0.6)

        # Group them both.
        end = VGroup(arrow, label).next_to(cells[len(cells) - 1], UP, buff=0.125)

        return end


class BubbleSort4(Scene):
    """
    Generate with:
    manim -ql --flush_cache bubble_sort.py BubbleSort4

    Add 2nd optimization (add a sorted flag)
    """
    def construct(self):
        # The list of numbers we want to sort in ascending order.
        list = [7, 4, 5, 6, 1, 2, 3]
        
        # Create a group of squares and a group of numbers.
        g_cells, g_nums = self.create_cells_and_numbers(list)

        # Create the arrows
        a1g, a2g = self.create_arrows(g_cells)

        # Create legends for the outer and inner loops.
        outer_loop = Text("outer loop - n:", font="Monospace").scale(0.5).to_edge(UL)
        inner_loop = (
            Text("inner loop - i:", font="Monospace")
            .scale(0.5)
            .next_to(outer_loop, DOWN)
        )
        indices = self.create_and_place_indices(g_cells)
        n_value = Integer(len(list) - 1).scale(0.8).next_to(outer_loop, RIGHT)
        i_value = Integer(0).scale(0.8).next_to(inner_loop, RIGHT)

        # Create 'n' arrow.
        n_arrow = self.create_n_arrow(g_cells)

        swapped_true = Text(
            'swapped: True', font="Monospace"
        ).scale(0.5).next_to(inner_loop, DOWN).to_edge(LEFT)

        swapped_false = Text(
            'swapped: False', font="Monospace"
        ).scale(0.5).next_to(inner_loop, DOWN).to_edge(LEFT)

        # Add all groups to the scene.
        self.add(
            g_cells,
            g_nums,
            a1g,
            a2g,
            outer_loop,
            n_value,
            inner_loop,
            i_value,
            indices,
            n_arrow,
            swapped_false,
        )

        n = len(g_nums) - 1
        while n > 0:
            swapped = False # Reset the flag.
            self.play(
                Circumscribe(n_value, Circle),
                n_value.animate.set_value(n),
                # Slide the end arrow under the last list item.
                n_arrow.animate.next_to(g_cells[n], UP, buff=0.125),
            )

            i = 0   # Reset the inner counter.
            while i < n:
                self.play(
                    # Slide the ARROWS under the list items being compared.
                    a1g.animate.next_to(g_cells[i], DOWN, buff=0.5),
                    a2g.animate.next_to(g_cells[i + 1], DOWN, buff=0.5),
                    # Update animation of inner loop counter.
                    Circumscribe(i_value, Circle),
                    i_value.animate.set_value(i)
                )

                # Once we've slided the ARROWS to their positions
                # Apply this animation only once, for the first outer loop iteration.
                if n == len(g_cells) - 1 and i == 0:
                    self.play(Circumscribe(swapped_false, Rectangle))
                elif i == 0:
                    if swapped_true in self.mobjects:
                        self.play(FadeOut(swapped_true))
                        self.play(
                            FadeIn(swapped_false),
                            Circumscribe(swapped_false, Rectangle)
                        )
                        self.remove(swapped_true)
                    else:
                        self.play(Circumscribe(swapped_false))

                # Change the background color of the squares to yellow.
                self.play(
                    g_cells[i].animate.set_fill(color=YELLOW, opacity=0.3),
                    g_cells[i + 1].animate.set_fill(color=YELLOW, opacity=0.3),
                )

                a = g_nums[i]
                b = g_nums[i + 1]
                # If the numbers are not in the right order (ascending)
                if a.get_value() > b.get_value():
                    swapped = True

                    # Change the background color of the squares to RED.
                    self.play(
                        g_cells[i].animate.set_fill(color=RED, opacity=0.3),
                        g_cells[i + 1].animate.set_fill(color=RED, opacity=0.3),
                    )

                    # Store the center of the Mobject to the left.
                    tmp = a.get_center()
                    # Swap the positions of the Mobjects.
                    self.play(
                        a.animate.move_to(b.get_center()),
                        b.animate.move_to(tmp),
                    )
                    # Swap the Mobjects in the VGroup.
                    g_nums[i], g_nums[i + 1] = g_nums[i + 1], g_nums[i]

                    if i == 0:
                        self.play(
                            FadeOut(swapped_false),
                            FadeIn(swapped_true),
                            Circumscribe(swapped_true, Rectangle),
                        )
                        self.remove(swapped_false)
                    else:
                        if swapped_true in self.mobjects:
                            self.play(Circumscribe(swapped_true, Rectangle))
                        else:
                            self.play(
                                FadeOut(swapped_false),
                                FadeIn(swapped_true),
                                Circumscribe(swapped_true, Rectangle)
                            )
                            self.remove(swapped_false)

                else:
                    # Change the background color of the squares to green.
                    self.play(
                        g_cells[i].animate.set_fill(color=GREEN, opacity=0.3),
                        g_cells[i + 1].animate.set_fill(color=GREEN, opacity=0.3),
                    )

                # Remove the red/green background.
                self.play(
                    g_cells[i].animate.set_fill(opacity=0),
                    g_cells[i + 1].animate.set_fill(opacity=0),
                )
                
                # Increment the inner counter.
                i += 1

            # Turn the last cell grey.
            self.play(
                g_cells[n].animate.set_color(GRAY),
                g_nums[n].animate.set_color(GRAY),
            )

            # Bail if the list is already sorted!
            if not swapped:
                break
            # Decrement the remaining amount of outer loop passes.
            n -= 1
    
    def create_and_place_indices(self, cells):
        indices = VGroup()

        for i, cell in enumerate(cells):
            n = Text(str(i), font='Monospace', fill_opacity=0.5).scale(0.4).next_to(cell, DOWN, buff=0.125).shift(LEFT * 0.25)
            indices.add(n)
        return indices

    def create_cells_and_numbers(self, list):
        # Create a group of squares and a group of numbers.
        g_cells = VGroup()
        g_nums = VGroup()

        # Traverse the list of numbers.
        for i in list:
            # Create a cell (Square Mobject).
            cell = Square(side_length=1, color=WHITE)

            # Make an Integer Mobject out of each number in the original list.
            num = Integer(i, color=WHITE)

            # For all the cells, other than the first one.
            if len(g_cells) > 0:
                # Position the cell right next to the previous square.
                cell.next_to(g_cells[-1], RIGHT, buff=0)

            # Move the integer Mobject to the center of the cell.
            num.move_to(cell.get_center())
            # Add the square to the list of cells.
            g_cells.add(cell)
            # Add the number to the list of numbers.
            g_nums.add(num)

        # Move the group of cells to the center.
        g_cells.move_to(ORIGIN)
        # Move the group of numbers to the center.
        g_nums.move_to(ORIGIN)

        return g_cells, g_nums

    def create_arrows(self, g_cells):
        # Create arrow 'i'.
        arrow = Arrow(
            start=DOWN,
            end=UP,
        ).scale(0.5, scale_tips=True)
        # Create a label for the arrow.
        label = Text("i", color=WHITE).next_to(arrow, DOWN, buff=0).scale(0.6)
        # Group them both.
        a1g = VGroup(arrow, label).next_to(g_cells[0], DOWN, buff=0.5)

        # Create arrow 'i+1'.
        arrow2 = arrow.copy()
        a2g = VGroup(
            arrow2, Text("i+1", color=WHITE).next_to(arrow2, DOWN, buff=0).scale(0.6)
        ).next_to(g_cells[1], DOWN, buff=0.5)

        return a1g, a2g
    
    def create_n_arrow(self, cells):
        # Create an arrow
        arrow = Arrow(
            start=UP,
            end=DOWN,
        ).scale(0.5, scale_tips=True)

        # Create a label for the arrow.
        label = Text("n", color=WHITE).next_to(arrow, UP, buff=0).scale(0.6)

        # Group them both.
        end = VGroup(arrow, label).next_to(cells[len(cells) - 1], UP, buff=0.125)

        return end

class BubbleSort5(Scene):
    """
    Generate with:
    manim -ql --flush_cache bubble_sort.py BubbleSort5

    Add 2nd optimization (add a sorted flag)
    """
    def construct(self):
        # The list of numbers we want to sort in ascending order.
        list = [7, 1, 2, 3, 4, 5, 6]
        
        # Create a group of squares and a group of numbers.
        g_cells, g_nums = self.create_cells_and_numbers(list)

        # Create the arrows
        a1g, a2g = self.create_arrows(g_cells)

        # Create legends for the outer and inner loops.
        outer_loop = Text("outer loop - n:", font="Monospace").scale(0.5).to_edge(UL)
        inner_loop = (
            Text("inner loop - i:", font="Monospace")
            .scale(0.5)
            .next_to(outer_loop, DOWN)
        )
        indices = self.create_and_place_indices(g_cells)
        n_value = Integer(len(list) - 1).scale(0.8).next_to(outer_loop, RIGHT)
        i_value = Integer(0).scale(0.8).next_to(inner_loop, RIGHT)

        # Create 'n' arrow.
        n_arrow = self.create_n_arrow(g_cells)

        swapped_true = Text(
            'swapped: True', font="Monospace"
        ).scale(0.5).next_to(inner_loop, DOWN).to_edge(LEFT)

        swapped_false = Text(
            'swapped: False', font="Monospace"
        ).scale(0.5).next_to(inner_loop, DOWN).to_edge(LEFT)

        # Add all groups to the scene.
        self.add(
            g_cells,
            g_nums,
            a1g,
            a2g,
            outer_loop,
            n_value,
            inner_loop,
            i_value,
            indices,
            n_arrow,
            swapped_false,
        )

        n = len(g_nums) - 1
        while n > 0:
            swapped = False # Reset the flag.
            self.play(
                Circumscribe(n_value, Circle),
                n_value.animate.set_value(n),
                # Slide the end arrow under the last list item.
                n_arrow.animate.next_to(g_cells[n], UP, buff=0.125),
            )

            i = 0   # Reset the inner counter.
            while i < n:
                self.play(
                    # Slide the ARROWS under the list items being compared.
                    a1g.animate.next_to(g_cells[i], DOWN, buff=0.5),
                    a2g.animate.next_to(g_cells[i + 1], DOWN, buff=0.5),
                    # Update animation of inner loop counter.
                    Circumscribe(i_value, Circle),
                    i_value.animate.set_value(i)
                )

                # Once we've slided the ARROWS to their positions
                # Apply this animation only once, for the first outer loop iteration.
                if n == len(g_cells) - 1 and i == 0:
                    self.play(Circumscribe(swapped_false, Rectangle))
                elif i == 0:
                    if swapped_true in self.mobjects:
                        self.play(FadeOut(swapped_true))
                        self.play(
                            FadeIn(swapped_false),
                            Circumscribe(swapped_false, Rectangle)
                        )
                        self.remove(swapped_true)
                    else:
                        self.play(Circumscribe(swapped_false))

                # Change the background color of the squares to yellow.
                self.play(
                    g_cells[i].animate.set_fill(color=YELLOW, opacity=0.3),
                    g_cells[i + 1].animate.set_fill(color=YELLOW, opacity=0.3),
                )

                a = g_nums[i]
                b = g_nums[i + 1]
                # If the numbers are not in the right order (ascending)
                if a.get_value() > b.get_value():
                    swapped = True

                    # Change the background color of the squares to RED.
                    self.play(
                        g_cells[i].animate.set_fill(color=RED, opacity=0.3),
                        g_cells[i + 1].animate.set_fill(color=RED, opacity=0.3),
                    )

                    # Store the center of the Mobject to the left.
                    tmp = a.get_center()
                    # Swap the positions of the Mobjects.
                    self.play(
                        a.animate.move_to(b.get_center()),
                        b.animate.move_to(tmp),
                    )
                    # Swap the Mobjects in the VGroup.
                    g_nums[i], g_nums[i + 1] = g_nums[i + 1], g_nums[i]

                    if i == 0:
                        self.play(
                            FadeOut(swapped_false),
                            FadeIn(swapped_true),
                            Circumscribe(swapped_true, Rectangle),
                        )
                        self.remove(swapped_false)
                    else:
                        if swapped_true in self.mobjects:
                            self.play(Circumscribe(swapped_true, Rectangle))
                        else:
                            self.play(
                                FadeOut(swapped_false),
                                FadeIn(swapped_true),
                                Circumscribe(swapped_true, Rectangle)
                            )
                            self.remove(swapped_false)

                else:
                    # Change the background color of the squares to green.
                    self.play(
                        g_cells[i].animate.set_fill(color=GREEN, opacity=0.3),
                        g_cells[i + 1].animate.set_fill(color=GREEN, opacity=0.3),
                    )

                # Remove the red/green background.
                self.play(
                    g_cells[i].animate.set_fill(opacity=0),
                    g_cells[i + 1].animate.set_fill(opacity=0),
                )
                
                # Increment the inner counter.
                i += 1

            # Turn the last cell grey.
            self.play(
                g_cells[n].animate.set_color(GRAY),
                g_nums[n].animate.set_color(GRAY),
            )

            # Bail if the list is already sorted!
            if not swapped:
                break
            # Decrement the remaining amount of outer loop passes.
            n -= 1
    
    def create_and_place_indices(self, cells):
        indices = VGroup()

        for i, cell in enumerate(cells):
            n = Text(str(i), font='Monospace', fill_opacity=0.5).scale(0.4).next_to(cell, DOWN, buff=0.125).shift(LEFT * 0.25)
            indices.add(n)
        return indices

    def create_cells_and_numbers(self, list):
        # Create a group of squares and a group of numbers.
        g_cells = VGroup()
        g_nums = VGroup()

        # Traverse the list of numbers.
        for i in list:
            # Create a cell (Square Mobject).
            cell = Square(side_length=1, color=WHITE)

            # Make an Integer Mobject out of each number in the original list.
            num = Integer(i, color=WHITE)

            # For all the cells, other than the first one.
            if len(g_cells) > 0:
                # Position the cell right next to the previous square.
                cell.next_to(g_cells[-1], RIGHT, buff=0)

            # Move the integer Mobject to the center of the cell.
            num.move_to(cell.get_center())
            # Add the square to the list of cells.
            g_cells.add(cell)
            # Add the number to the list of numbers.
            g_nums.add(num)

        # Move the group of cells to the center.
        g_cells.move_to(ORIGIN)
        # Move the group of numbers to the center.
        g_nums.move_to(ORIGIN)

        return g_cells, g_nums

    def create_arrows(self, g_cells):
        # Create arrow 'i'.
        arrow = Arrow(
            start=DOWN,
            end=UP,
        ).scale(0.5, scale_tips=True)
        # Create a label for the arrow.
        label = Text("i", color=WHITE).next_to(arrow, DOWN, buff=0).scale(0.6)
        # Group them both.
        a1g = VGroup(arrow, label).next_to(g_cells[0], DOWN, buff=0.5)

        # Create arrow 'i+1'.
        arrow2 = arrow.copy()
        a2g = VGroup(
            arrow2, Text("i+1", color=WHITE).next_to(arrow2, DOWN, buff=0).scale(0.6)
        ).next_to(g_cells[1], DOWN, buff=0.5)

        return a1g, a2g
    
    def create_n_arrow(self, cells):
        # Create an arrow
        arrow = Arrow(
            start=UP,
            end=DOWN,
        ).scale(0.5, scale_tips=True)

        # Create a label for the arrow.
        label = Text("n", color=WHITE).next_to(arrow, UP, buff=0).scale(0.6)

        # Group them both.
        end = VGroup(arrow, label).next_to(cells[len(cells) - 1], UP, buff=0.125)

        return end

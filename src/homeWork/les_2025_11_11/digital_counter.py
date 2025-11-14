# DZ 13.2. Class "Digital Counter"
class Counter:
    """
    Counter class with setting min, max, current value
    and step increment/decrement with checking for ValueError.
    """

    def __init__(self, current: int = 1, min_value: int = 0, max_value: int = 10) -> None:
        """
        Initialize the counter.

        current: Initial value of the counter
        min_value: Minimum value
        max_value: Maximum value
        ValueError: If current is outside the range [min_value, max_value]
        """
        self.current = current
        self.min_value = min_value
        self.max_value = max_value
        if current < min_value or current > max_value:
            raise ValueError("The current value is outside the minimum or maximum limits.")

    def set_current(self, start: int) -> None:
        """
        start: New current value
        """
        self.current = start

    def set_max(self, max_max: int) -> None:
        """
        Set the maximum value of the counter.
        max_max: New maximum
        ValueError: If max_max is less than min_value
        or current is greater than the new maximum
        """
        if max_max < self.min_value:
            raise ValueError("The maximum cannot be less than the minimum.")
        if self.current > max_max:
            raise ValueError("Current value exceeds new maximum.")
        self.max_value = max_max

    def set_min(self, min_min: int) -> None:
        """
        Sets the minimum value of the counter.
        min_min: New minimum
        ValueError: If min_min is greater
        than max_value or current is less than the new minimum
        """
        if min_min > self.max_value:
            raise ValueError("The minimum cannot be greater than the maximum.")
        if self.current < min_min:
            raise ValueError("Current value is less than new minimum.")
        self.min_value = min_min

    def step_up(self) -> None:
        """
        Increases the current value by 1.
        """
        if self.current == self.max_value:
            raise ValueError("Maximum reached.")
        self.current += 1

    def step_down(self) -> None:
        """
        Decreases the current value by 1.
        """
        if self.current == self.min_value:
            raise ValueError("Minimum reached.")
        self.current -= 1

    def get_current(self) -> int:
        """
        Returns the current value of the counter.
        """
        return self.current


# ---Перевірка---
counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
print(counter.get_current())  # == 10, 'Test1'
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e)  # Достигнут максимум
print(counter.get_current())  # == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
print(counter.get_current())  # == 7, 'Test3'
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e)  # Достигнут минимум
print(counter.get_current())  # == 7, 'Test4'

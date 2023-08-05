from __future__ import annotations

from pylav.filters.utils import FilterMixin


class ChannelMix(FilterMixin):
    __slots__ = ("_left_to_left", "_left_to_right", "_right_to_left", "_right_to_right", "_off", "_default")

    def __init__(
        self,
        left_to_left: float,
        left_to_right: float,
        right_to_left: float,
        right_to_right: float,
    ):
        super().__init__()
        self.left_to_left = left_to_left
        self.left_to_right = left_to_right
        self.right_to_left = right_to_left
        self.right_to_right = right_to_right
        self.off = False

    def to_dict(self) -> dict:
        return {
            "leftToLeft": self.left_to_left,
            "leftToRight": self.left_to_right,
            "rightToLeft": self.right_to_left,
            "rightToRight": self.right_to_right,
            "off": self.off,
        }

    def to_json(self) -> dict:
        return {
            "leftToLeft": self.left_to_left,
            "leftToRight": self.left_to_right,
            "rightToLeft": self.right_to_left,
            "rightToRight": self.right_to_right,
        }

    @classmethod
    def from_dict(cls, data: dict) -> ChannelMix:
        c = cls(
            left_to_left=data["leftToLeft"],
            left_to_right=data["leftToRight"],
            right_to_left=data["rightToLeft"],
            right_to_right=data["rightToRight"],
        )
        c.off = data["off"]
        return c

    def __repr__(self):
        return (
            f"<ChannelMix: left_to_left={self.left_to_left}, "
            f"left_to_right={self.left_to_right}, "
            f"right_to_left={self.right_to_left}, "
            f"right_to_right={self.right_to_right}>"
        )

    @property
    def left_to_left(self) -> float:
        return self._left_to_left

    @left_to_left.setter
    def left_to_left(self, v: float):
        self._left_to_left = v
        self.off = False

    @property
    def left_to_right(self) -> float:
        return self._left_to_right

    @left_to_right.setter
    def left_to_right(self, v: float):
        self._left_to_right = v
        self.off = False

    @property
    def right_to_left(self) -> float:
        return self._right_to_left

    @right_to_left.setter
    def right_to_left(self, v: float):
        self._right_to_left = v
        self.off = False

    @property
    def right_to_right(self) -> float:
        return self._right_to_right

    @right_to_right.setter
    def right_to_right(self, v: float):
        self._right_to_right = v
        self.off = False

    @classmethod
    def default(cls) -> ChannelMix:
        c = cls(
            left_to_left=-31415926543,
            left_to_right=-31415926543,
            right_to_left=-31415926543,
            right_to_right=-31415926543,
        )
        c.off = True
        return c

    def get(self) -> dict[str, float]:
        if self.off:
            return {}
        return {
            "leftToLeft": self.left_to_left,
            "leftToRight": self.left_to_right,
            "rightToLeft": self.right_to_left,
            "rightToRight": self.right_to_right,
        }

    def reset(self) -> None:
        self.right_to_right = self.right_to_left = self.left_to_right = self.left_to_left = -31415926543
        self.off = True

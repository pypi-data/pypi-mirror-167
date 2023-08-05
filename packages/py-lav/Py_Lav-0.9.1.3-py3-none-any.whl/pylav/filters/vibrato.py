from __future__ import annotations

from pylav.filters.utils import FilterMixin


class Vibrato(FilterMixin):
    __slots__ = ("_frequency", "_depth", "_off", "_default")

    def __init__(self, frequency: float, depth: float):
        super().__init__()
        self.frequency = frequency
        self.depth = depth
        self.off = False

    def to_dict(self) -> dict:
        return {
            "frequency": self.frequency,
            "depth": self.depth,
            "off": self.off,
        }

    def to_json(self) -> dict:
        return {
            "frequency": self.frequency,
            "depth": self.depth,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Vibrato:
        c = cls(frequency=data["frequency"], depth=data["depth"])
        c.off = data["off"]
        return c

    def __repr__(self):
        return f"<Vibrato: frequency={self.frequency}, depth={self.depth}>"

    @property
    def frequency(self) -> float:
        return self._frequency

    @frequency.setter
    def frequency(self, v: float):
        if v == -31415926543:
            self.off = True
            self._frequency = v
            return
        if not (0.0 < v <= 14.0):
            raise ValueError(f"Frequency must be must be 0.0 < v <= 14.0, not {v}")
        self._frequency = v
        self.off = False

    @property
    def depth(self) -> float:
        return self._depth

    @depth.setter
    def depth(self, v: float):
        if v == -31415926543:
            self.off = True
            self._depth = v
            return
        if not (0.0 < v <= 1.0):
            raise ValueError(f"Depth must be must be 0.0 < x ≤ 1.0, not {v}")
        self._depth = v
        self.off = False

    @classmethod
    def default(cls) -> Vibrato:
        c = cls(frequency=-31415926543, depth=-31415926543)
        c.off = True
        return c

    def get(self) -> dict[str, float]:
        return (
            {}
            if self.off
            else {
                "frequency": self.frequency,
                "depth": self.depth,
            }
        )

    def reset(self) -> None:
        self.frequency = self.depth = -31415926543
        self.off = True

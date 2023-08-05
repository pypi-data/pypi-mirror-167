from __future__ import annotations

from pylav.filters.utils import FilterMixin


class Rotation(FilterMixin):
    __slots__ = ("_hertz", "_off", "_default")

    def __init__(self, hertz: float):
        super().__init__()
        self.hertz = hertz
        self.off = False

    def to_dict(self) -> dict:
        return {
            "hertz": self.hertz,
            "off": self.off,
        }

    def to_json(self) -> dict:
        return {
            "hertz": self.hertz,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Rotation:
        c = cls(hertz=data["hertz"])
        c.off = data["off"]
        return c

    def __repr__(self):
        return f"<Rotation: hertz={self.hertz}>"

    @property
    def hertz(self) -> float:
        return self._hertz

    @hertz.setter
    def hertz(self, v: float):
        self._hertz = v
        self.off = False

    @classmethod
    def default(cls) -> Rotation:
        c = cls(hertz=-31415926543)
        c.off = True
        return c

    def get(self) -> dict[str, float]:
        return (
            {}
            if self.off
            else {
                "rotationHz": self.hertz,
            }
        )

    def reset(self) -> None:
        self.hertz = -31415926543
        self.off = True

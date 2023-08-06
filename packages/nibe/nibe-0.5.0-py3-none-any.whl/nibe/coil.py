from typing import Dict, Optional, Union

from construct import (
    ConstructError,
    Int8sl,
    Int8ul,
    Int16sl,
    Int16ul,
    Int32sl,
    Int32ul,
    Padded,
)

from nibe.exceptions import DecodeException, EncodeException
from nibe.parsers import WordSwapped

parser_map = {
    "u8": Int8ul,
    "s8": Int8sl,
    "u16": Int16ul,
    "s16": Int16sl,
    "u32": Int32ul,
    "s32": Int32sl,
}

parser_map_word_swaped = parser_map.copy()
parser_map_word_swaped.update(
    {
        "u32": WordSwapped(Int32ul),
        "s32": WordSwapped(Int32sl),
    }
)


def is_coil_boolean(coil):
    if coil.factor != 1:
        return False

    if coil.min == 0 and coil.max == 1:
        return True

    if coil.mappings and all(k in ["0", "1"] for k in coil.mappings):
        return True

    return False


class Coil:
    mappings: Optional[Dict[str, str]]
    reverse_mappings: Optional[Dict[str, str]]

    def __init__(
        self,
        address: int,
        name: str,
        title: str,
        size: str,
        factor: int = 1,
        info: str = None,
        unit: str = None,
        mappings: dict = None,
        write: bool = False,
        word_swap: bool = True,
        **kwargs,
    ):
        assert isinstance(address, int), "Address must be defined"
        assert name, "Name must be defined"
        assert title, "Title must be defined"
        assert factor, "Factor must be defined"
        assert not (
            mappings is not None and factor != 1
        ), "When mapping is used factor needs to be 1"

        self.size = size
        if word_swap:
            self.parser = parser_map.get(size)
        else:
            self.parser = parser_map_word_swaped.get(size)

        assert self.parser is not None

        self.address = address
        self.name = name
        self.title = title
        self.factor = factor

        self.set_mappings(mappings)

        self.info = info
        self.unit = unit
        self.is_writable = write

        self.other = kwargs

        self.raw_min = self.other.get("min")
        self.raw_max = self.other.get("max")

        self.min = self.raw_min / factor if self.raw_min is not None else None
        self.max = self.raw_max / factor if self.raw_max is not None else None

        self.is_boolean = is_coil_boolean(self)
        if self.is_boolean and not mappings:
            self.set_mappings({"0": "OFF", "1": "ON"})

        self._value = None

    def set_mappings(self, mappings):
        if mappings:
            self.mappings = dict((k, v.upper()) for k, v in mappings.items())
            self.reverse_mappings = dict((v.upper(), k) for k, v in mappings.items())
        else:
            self.mappings = None
            self.reverse_mappings = None

    @property
    def value(self) -> Union[int, float, str, None]:
        return self._value

    @value.setter
    def value(self, value: Union[int, float, str, None]):
        if value is None:
            self._value = None
            return

        if self.mappings:
            value = value.upper()
            assert (
                value in self.reverse_mappings
            ), f"Provided value '{value}' is not in {self.reverse_mappings.keys()} for {self.name}"

            self._value = value
            return

        assert isinstance(
            value, (int, float)
        ), f"Provided value '{value}' is invalid type (int and float are supported) for {self.name}"

        self.check_value_bounds(value)

        self._value = value

    @property
    def raw_value(self) -> bytes:
        return self._encode(self.value)

    @raw_value.setter
    def raw_value(self, raw_value: bytes):
        self.value = self._decode(raw_value)

    def _decode(self, raw: bytes) -> Union[int, float, str]:
        value = self.parser.parse(raw)
        if self._is_hitting_integer_limit(value):
            return None
        try:
            self._check_raw_value_bounds(value)
        except AssertionError as e:
            raise DecodeException(
                f"Failed to decode {self.name} coil from raw: {raw}, exception: {e}"
            )
        if self.factor != 1:
            value /= self.factor
        if self.mappings is None:
            return value

        mapped_value = self.mappings.get(str(value))
        if mapped_value is None:
            raise DecodeException(
                f"Mapping not found for {self.name} coil for value: {value}"
            )

        return mapped_value

    def _is_hitting_integer_limit(self, int_value: int):
        if self.size == "u8" and int_value == 0xFF:
            return True
        if self.size == "s8" and int_value == -0x80:
            return True
        if self.size == "u16" and int_value == 0xFFFF:
            return True
        if self.size == "s16" and int_value == -0x8000:
            return True
        if self.size == "u32" and int_value == 0xFFFFFFFF:
            return True
        if self.size == "s32" and int_value == -0x80000000:
            return True

        return False

    def _encode(self, value: Union[int, float, str, None]) -> bytes:
        try:
            assert value is not None, "Unable to encode None value"
            if self.reverse_mappings is not None:
                mapped_value = self.reverse_mappings.get(str(value))
                assert mapped_value is not None, "Mapping not found"

                return self._pad(mapped_value)

            if self.factor != 1:
                value *= self.factor

            self._check_raw_value_bounds(value)

            return self._pad(value)
        except (ConstructError, AssertionError) as e:
            raise EncodeException(
                f"Failed to encode {self.name} coil for value: {value}, exception: {e}"
            )

    def _pad(self, value) -> bytes:
        return Padded(4, self.parser).build(int(value))

    def check_value_bounds(self, value):
        if self.min is not None:
            assert (
                value >= self.min
            ), f"{self.name} coil value ({value}) is smaller than min allowed ({self.min})"

        if self.max is not None:
            assert (
                value <= self.max
            ), f"{self.name} coil value ({value}) is larger than max allowed ({self.max})"

    def _check_raw_value_bounds(self, value):
        if self.raw_min is not None:
            assert (
                value >= self.raw_min
            ), f"value ({value}) is smaller than min allowed ({self.raw_min})"

        if self.raw_max is not None:
            assert (
                value <= self.raw_max
            ), f"value ({value}) is larger than max allowed ({self.raw_max})"

    def __repr__(self):
        return f"Coil {self.address}, name: {self.name}, title: {self.title}, value: {self.value}"

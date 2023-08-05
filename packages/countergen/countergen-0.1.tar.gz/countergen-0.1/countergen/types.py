import abc
from typing import Any, Callable, Generic, Iterable, NamedTuple, Optional, Sequence, TextIO, TypeVar
from attrs import define

Input = str  # The input to an NLP mode
Output = list[str]  # The different acceptable outputs of the NLP, string label or number, but in string format

Performance = float  # usually between zero & one (one is better)
ModelEvaluator = Callable[[Input, Output], Performance]

Category = str  # The different kinds of data produced by converters


class Converter(metaclass=abc.ABCMeta):
    @abc.abstractproperty
    def categories(self) -> tuple[Category, Category]:
        ...

    @abc.abstractmethod
    def convert_to(self, inp: Input, to: Category) -> Input:
        ...


class Variation(NamedTuple):
    text: Input
    categories: tuple[Category, ...]


class AugmentedSample(metaclass=abc.ABCMeta):
    @abc.abstractproperty
    def input(self) -> Input:
        ...

    @abc.abstractproperty
    def expected_output(self) -> Output:
        ...

    @abc.abstractmethod
    def get_variations(self) -> Sequence[Variation]:
        ...


SampleResults = Iterable[tuple[Performance, tuple[Category, ...]]]
Results = Iterable[SampleResults]

T = TypeVar("T")


class StatsAgregator(Generic[T], metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __call__(self, performances: Results) -> T:
        ...

    @abc.abstractmethod
    def save_agregation(self, performances: Results, file: Optional[TextIO] = None):
        ...

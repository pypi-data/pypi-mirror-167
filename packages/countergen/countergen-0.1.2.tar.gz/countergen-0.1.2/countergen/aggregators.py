from collections import defaultdict
from statistics import geometric_mean
from typing import Any, Iterable, Mapping, Optional, Sequence, TextIO, TypeVar
from attrs import define
from countergen.plot_utils import plot_mutli_bars

from countergen.types import (
    AugmentedSample,
    Category,
    ModelEvaluator,
    Performance,
    Results,
    StatsAggregator,
)
from countergen.utils import mean


@define
class AveragePerformancePerCategory(StatsAggregator):
    use_geometric_mean: bool = False

    def __call__(self, performances: Results) -> Mapping[Category, float]:
        performances_per_category: defaultdict[Category, list[float]] = defaultdict(lambda: [])
        for sample_perfs in performances:
            for perf, categories in sample_perfs:
                for c in categories:
                    performances_per_category[c].append(perf)

        mean_ = geometric_mean if self.use_geometric_mean else mean
        avg_performances_per_category = {c: mean_(perfs) for c, perfs in performances_per_category.items()}
        return avg_performances_per_category

    def save_aggregation(self, aggregate: Mapping[Category, float], file: Optional[TextIO] = None):
        print("Average performance per category:", file=file)
        for c, perf in aggregate.items():
            print(f"{c}: {perf:.6f}", file=file)

    def load_aggregation(self, file: TextIO) -> Mapping[Category, float]:
        lines = file.readlines()
        r = {}
        for l in lines[1:]:
            c, p = l.split(": ")
            r[c] = float(p)
        return r

    def display(self, aggregates: Mapping[str, Mapping[Category, float]]):
        plot_mutli_bars(aggregates, xlabel="Model name", ylabel="Performance", title="Performance by model & category")


@define
class AverageDifference(StatsAggregator):
    positive_category: Category
    negative_category: Category
    relative_difference: bool = False

    def __call__(self, performances: Results) -> float:
        differences = []
        for sample_perfs in performances:
            positive_perfs = [perf for perf, categories in sample_perfs if self.positive_category in categories]
            negative_perfs = [perf for perf, categories in sample_perfs if self.negative_category in categories]
            if positive_perfs and negative_perfs:
                diff = mean(positive_perfs) - mean(negative_perfs)
                if self.relative_difference:
                    diff /= mean(positive_perfs)
                differences.append(diff)
        return mean(differences)

    def save_aggregation(self, aggregate: float, file: Optional[TextIO] = None):
        relative = "relative " if self.relative_difference else ""
        print(
            f"The {relative}performance between category {self.positive_category} and category {self.negative_category}:",
            file=file,
        )
        print(f"{aggregate:.6f}", file=file)

    def load_aggregation(self, file: TextIO) -> float:
        lines = file.readlines()
        return float(lines[1])

    def display(self, aggregates: Mapping[str, float]):
        pass


# DOESN'T WORK EASILY because you have to split the file.

# @define
# class MultipleStatsAggregator(StatsAggregator):
#     aggregators: list[StatsAggregator]

#     def __call__(self, performances: Results) -> list[Any]:
#         return [ag(performances) for ag in self.aggregators]

#     def save_aggregation(self, aggregate: list[Any], file: Optional[TextIO] = None):
#         for ag in self.aggregators:
#             ag.save_aggregation(aggregate, file)

#     def load_aggregation(self, file: TextIO) -> list[Any]:
#         return [ag.load_aggregation(file) for ag in self.aggregators]

#     def display(self, aggregates: Sequence[list[Any]]):
#         for ag in self.aggregators:
#             ag.display(aggregates)

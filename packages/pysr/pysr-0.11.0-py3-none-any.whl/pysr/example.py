import math
from pysr import PySRRegressor

model = PySRRegressor(
    binary_operators="+ * / -".split(" "),
    unary_operators=["sqrt", "square"],
    populations=256,
    niterations=1000,
    ncyclesperiteration=5000,
    procs=128,
    # High precision:
    precision=64,
    # Favor simpler expressions:
    parsimony=0.001,
    # Disable constants:
    complexity_of_constants=100,
    # Prevent redundant computation:
    weight_mutate_constant=0.0,
    should_optimize_constants=False,
)

model.fit(
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],
    [math.pi],
    variable_names=["_1", "_2", "_3", "_4", "_5", "_6", "_7", "_8", "_9", "_10"],
)

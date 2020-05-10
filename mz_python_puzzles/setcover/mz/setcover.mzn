int: N;
set of int: ITEMS = 1..N;
int: M;
set of int: SETS = 1..M;
array[SETS] of int: cost;
array[SETS] of set of ITEMS: items_covered;

array[SETS] of var 0..1: chosen;

var int: obj = sum (s in SETS) (cost[s] * chosen[s]);
solve minimize obj;

constraint
    forall (i in ITEMS) (
        sum (s in SETS) ((i in items_covered[s]) * chosen[s]) >= 1
    );

output(
    ["\(obj)\n"]
    ++ [show(chosen[s]) ++ " " | s in SETS]
    ++ ["\n"]
);

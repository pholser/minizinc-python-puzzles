include "globals.mzn";

/* Dimension of a sub-square */
int: UNIT;
set of int: UNITS = 1..UNIT;

/* Dimension of the whole square */
int: SIZE = UNIT * UNIT;

set of int: DIGIT = 1..SIZE;

/* Known fixed points */
int: FIXED;
set of int: FIXED_POINTS = 1..FIXED;
array[FIXED_POINTS, 1..3] of DIGIT: fixed_points;


/* Fill in the grid */
array[DIGIT, DIGIT] of var DIGIT: grid;
solve satisfy;

/* Subject to... */

/* Unique values in rows */
constraint
    forall (r in DIGIT) (
        alldifferent([grid[r, c] | c in DIGIT])
    );

/* Unique values in columns */
constraint
    forall (c in DIGIT) (
        alldifferent([grid[r, c] | r in DIGIT])
    );

/* Unique values in sub-squares */
constraint
    forall (x in 0..UNIT-1, y in 0..UNIT-1) (
        alldifferent(
            [grid[x * UNIT + r, y * UNIT + c] | r in UNITS, c in UNITS]
        )
    );

/* Fixed points in place. */
constraint
    forall (f in FIXED_POINTS) (
        grid[fixed_points[f, 1], fixed_points[f, 2]] == fixed_points[f, 3]
    );

output(
   [ show(fix(grid[r, c])) ++ if c == SIZE then "\n" else " " endif
       | r in DIGIT, c in DIGIT ]);

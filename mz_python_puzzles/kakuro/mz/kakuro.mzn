include "globals.mzn";

set of int: DIGIT = 1..9;

/* Cells are blank squares that need to be filled in. */
int: number_of_cells;
set of int: CELL = 1..number_of_cells;

/* "Groups" correspond to rows or columns, that have sums
    associated with them. The specific rows and columns are not
    needed in this model. */
int: number_of_groups;
set of int: GROUP = 1..number_of_groups;
array[GROUP] of set of CELL: groups;
array[GROUP] of int: sums;

/* Fill in each cell with a digit. */
array[CELL] of var DIGIT: digits;

solve satisfy;

/* Digits distinct within a group. */
constraint
    forall (g in GROUP) (
        alldifferent([digits[c] | c in groups[g]])
    );

/* Digits in a group sum to a specified value. */
constraint
    forall (g in GROUP) (
        sum ([digits[c] | c in groups[g]]) == sums[g]
    );

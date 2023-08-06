# datagrid

Open source DataGrid implementation

## Installation

```
git clone git@github.com:comet-ml/datagrid.git
cd datagrid
pip install -e .
```

## Running Server

In the datagrid repo folder, run:

```
datagrid server
```

That runs the server on port 4001. That will serve any DataGrid in the
current directory by filename.

## Testing

In one terminal, run:

```
datagrid server --frontend no --open no
```

In a separate terminal, run:

```
datagrid viewer
```

to see a list of DataGrid files being served. Assume that
"images.datagrid" is listed. Then run:

```
datagrid viewer images.datagrid
```

That will show the first 10 rows of images.datagrid.

Other `datagrid viewer` flags:

```
optional arguments:
  -h, --help            show this help message and exit
  --port PORT
  --debug
  --width WIDTH
  --offset OFFSET
  --group-by GROUP_BY
  --where-expr WHERE_EXPR
  --limit LIMIT
  --sort-by SORT_BY
  --sort-desc
  --select SELECT [SELECT ...]
  --query-type QUERY_TYPE
  --column-name COLUMN_NAME
  --column-value COLUMN_VALUE
  --column-offset COLUMN_OFFSET
  --column-limit COLUMN_LIMIT
  --asset-id ASSET_ID
  --computed-columns COMPUTED_COLUMNS
```

Developer Notes:

1. computed-columns and where-expr can use DataGrid Python query expressions
2. DataGrid Python query expressions use the format `{"Column Name"}` to refer
    to a column, and can use Python expressions, including math ("math.sqrt"),
    Python functions (like "abs", "min", "max", "round").
3. DataGrid query expressions can use aggregate functions: AVG, MAX, MIN,
    SUM, TOTAL, and COUNT.
4. computed-columns are defined as a dictionary mapping a column's name
    to a dictionary with "expr", "field", and "type" defined.

Developer Examples:

```
# Create a virtual column called "Average Score" that is the
# aggregate Average value of the Score column.

data viewer images.datagrid \
    --computed-columns '{"Average Score": \
          {"field": "cc1", \
	   "expr": "AVG({\"Score\"})," \
	   "type": "FLOAT"}}'

# Create a virtual column called "Average Score" that is the
# aggregate Average value of the Score column, and filter
# on those rows where the Score is above average.

data viewer images.datagrid \
    --computed-columns '{"Average Score": \
          {"field": "cc1", \
	   "expr": "AVG({\"Score\"})," \
	   "type": "FLOAT"}}' \
    --where-exp '{"Score"} - {"Average Score"} > 0'
```

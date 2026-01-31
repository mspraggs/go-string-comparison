# Go string comparison benchmarks

Generates Go string comparison benchmarks for strings up to forty characters in
length.

## Usage

To gather benchmark data:

```
$ go test -count 10 -bench . | tee output.txt
```

To analyse the results, install Python requirements:

```
$ pip install -r requirements.txt
```

Run the analysis:

```
$ python analysis.py output.txt
```

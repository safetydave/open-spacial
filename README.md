# open-spacial
ThoughtWorks Shokunin Challenge April 2020

Example of reaching the food truck in a crowded office.

![I can haz food truck](https://raw.githubusercontent.com/safetydave/open-spacial/master/doc/trial_0.6_graph_pos_2.png)

Example of being unable to reach the food truck in a nearly empty office.

![I can NOT haz food truck](https://raw.githubusercontent.com/safetydave/open-spacial/master/doc/trial_0.1_graph_neg_1.png)

## Running Submission

### Set up Environment and Dependencies

1. Clone this repo (to `./open-spacial`)
2. Create and activate a Python 3.6+ Virtual Environment (`virtualenv -p python3 open-spacial`
   then `source open-spacial/bin/activate`
3. From repo base directory (`cd open-spacial`)
4. Run `pip install .`

### To Execute

```
cd src
python openspacial.py
```

### To Run Tests

```
cd test
python -m unittest discover .
```

## Results

From a selected run:
```
Number of samples for each p: 10000
1.0 0.000
0.9 0.000
0.8 0.000
0.7 0.000
0.6 0.006
0.5 0.062
0.4 0.356
0.3 0.811
0.2 0.964
0.1 0.996
0.0 1.000
```


## Awesomeness Criteria

### 1. Solving the Problem

Looks like a plausible solution. Tests and inspected visualised examples give confidence the results are correct. The results are similar to the problem statement. However, statistical analysis (below) shows it's almost impossible that my solution would generate the same results as the problem statement. 

### 2. Clean Code

I have aimed for clean code by using high-level abstractions supported by common Python libraries. 

I represented the empty office as a gridded graph with nodes for desks, joined by undirected edges to neighbours left, right, front and back. Occupied desks (and their connected edges) are removed from the graph. This was because - although I assume you can move any distance in any direction outside exclusion zones - when horizontally, vertically or diagonally adjacent desks are occupied nearby, your movements are effectively limited to the cardinal directions between desks. The food truck (target) is an additional node connected to every node in the front row and can be reached from your seat (source) if there is a path. Also, this is how it was drawn in the problem statement. :)

Note the submitted code is supported by exploratory work in Jupyter notebooks, included in the doc folder:

* The [exploratory notebook](doc/OpenSpacial.pdf) tests the problem framing, and includes visualisations and further statistical analysis of the proportions of available paths as a binomial distribution.
* The [many runs analysis](doc/ManyRuns.pdf) examines the results of many runs of the solution to build a normal approximation to the distribution of available paths for each value of p. Then we can test whether a given set of results is likely to be from this distribution. 

### 3. Evidence of TDD

The submitted code is supported by and driven by tests including:

* Deterministic unit tests
* Statistical unit tests to provide some level of assurance that observed results are drawn from an expected distribution. These tests are applied to random selection of source seat (`TestOccupancy.test_source_distribution`) and office seating (`TestOccupancy.test_seating_distribution`).
* Visual inspection tests which provide positive and negative examples of available paths for random occupancies at each value of p (`TrialRunner.draw_case()`).

My learning objectives included migrating notebook sketches to properly structured Python projects including a range of tests suitable for analytics applications. I made some progress.

### 4. Still working on the go script...

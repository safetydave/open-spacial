import pandas as pd

from ospacial.trialrunner import TrialRunner


def run_one():
    trials = 10000
    # occupancy proportions to test
    ps = [x / 10.0 for x in range(11)]
    ps.reverse()

    tr = TrialRunner(trials, ps)
    tr.run()
    print(tr.summary())


def run_many():
    trials = 10000
    # occupancy proportions to test
    ps = [x / 10.0 for x in range(11)]
    ps.reverse()

    runs_results = []

    for i in range(200):
        print('Run {}'.format(i))
        tr = TrialRunner(trials, ps)
        tr.run()
        print(tr.summary())
        runs_results.append(tr.results)

    df = pd.DataFrame(runs_results, columns=['{:.1f}'.format(p) for p in ps])
    df.to_csv('runs.csv')


if __name__ == "__main__":
    run_one()

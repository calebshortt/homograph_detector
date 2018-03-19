
import statistics

from base.results import ResultSet


class Engine(object):

    """

    Flow:
        1. Take in a string (URL)
        2. Analyze the char ints for each char
        3. Calculate the mean, median, stdev, etc
        4. Try to find any ASCII chars that shouldn't be there (different language or soemthing)

    """

    results = {}
    threshold_std = 1

    def __init__(self):
        pass

    def analyze(self, string):

        ints = [ord(char) for char in string]

        max_char = max(ints)
        min_char = min(ints)
        mean = statistics.mean(ints)
        median = statistics.median(ints)
        stdev = statistics.stdev(ints)

        return ResultSet(r_max=max_char, r_min=min_char, mean_means=mean, mean_medians=median, mean_stdevs=stdev)

    def load_strings(self, filepath):
        strings = []
        with open(filepath, 'r') as f:
            for line in f:
                strings.append(str(line).strip())

        return strings

    def analyze_many(self, filepath):
        strings = self.load_strings(filepath)
        results = []
        for string in strings:
            results.append(self.analyze(string))

        self.results = ResultSet(**self.run_stats(results))
        return self.results

    def run_stats(self, result_set):

        mx = 0
        mn = 99999999
        means = []
        medians = []
        stdevs = []

        # for tmp_mx, tmp_mn, tmp_mean, tmp_median, tmp_stdev in result_set:
        for res in result_set:
            mx = max(res.result_max, mx)
            mn = min(res.result_min, mn)
            means.append(res.mean_means)
            medians.append(res.mean_medians)
            stdevs.append(res.mean_stdevs)

        return {
            'r_max': mx, 'r_min': mn,
            'mean_means': statistics.mean(means), 'stdev_means': statistics.stdev(means),
            'mean_medians': statistics.mean(medians), 'stdev_medians': statistics.stdev(medians),
            'mean_stdevs': statistics.mean(stdevs), 'stdev_stdevs': statistics.stdev(stdevs)
        }

    def test_string(self, string):
        """
        Test the given string against the calculated result set
        :param string:
        :return: decision (boolean), calculated results
        """

        string_stats = self.analyze(string)
        return self.results.compare(string_stats)

    def test_strings(self, filepath):
        results = []
        strings = self.load_strings(filepath)
        for string in strings:
            results.append(self.test_string(string))
        return results


if __name__ == "__main__":
    engine = Engine()

    results = engine.analyze_many("../resources/urls.txt")
    print('Corpus Stats: \n'
          'Labels: [(max, min), (mean of means, std of means), (mean of medians, std of medians), (mean od stds, std of stds)]'
          '\n%s' % results.all_stats)

    print('\n\nTesting...\n'
          'Labels: (accepted?, <stats like above>, reason for failure (if there is one))')

    print(engine.test_string('www.fаcebook.com'))

    # test_results = engine.test_strings('../resources/known_external.txt')
    #
    # for r in test_results:
    #     print(r)
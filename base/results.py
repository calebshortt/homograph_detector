

class ResultSet(object):

    result_max = None
    result_min = None
    mean_means = None
    stdev_means = None
    mean_medians = None
    stdev_medians = None
    mean_stdevs = None
    stdev_stdevs = None

    all_stats = []

    def __init__(self, *args, **kwargs):
        self.result_max = kwargs.get('r_max', 0)
        self.result_min = kwargs.get('r_min', 999999)
        self.mean_means = kwargs.get('mean_means', 0.0)
        self.stdev_means = kwargs.get('stdev_means', 0.0)
        self.mean_medians = kwargs.get('mean_medians', 0.0)
        self.stdev_medians = kwargs.get('stdev_medians', 0.0)
        self.mean_stdevs = kwargs.get('mean_stdevs', 0.0)
        self.stdev_stdevs = kwargs.get('stdev_stdevs', 0.0)

        self.all_stats = [
            (self.result_max, self.result_min),
            (self.mean_means, self.stdev_means),
            (self.mean_medians, self.stdev_medians),
            (self.mean_stdevs, self.stdev_stdevs),
        ]

    def compare(self, str_stats, stdev_threshold=2):
        """

        :param str_stats: ResultSet object
        :param stdev_threshold: (int) number of standard deviations allowed
        :return:
        """

        print('Analysing: Threshold: 2 standard deviations...')

        str_max = str_stats.result_max
        str_min = str_stats.result_min
        str_mean = str_stats.mean_means
        str_median = str_stats.mean_medians
        str_stdev = str_stats.mean_stdevs

        if not (self.result_min <= str_min <= str_max <= self.result_max):
            return False, str_stats.all_stats, 'max/min range'

        r_mean_low = self.mean_means - stdev_threshold*self.stdev_means
        r_mean_high = self.mean_means + stdev_threshold*self.stdev_means
        if not (r_mean_low <= str_mean <= r_mean_high):
            return False, str_stats.all_stats, 'mean'

        r_median_low = self.mean_medians - stdev_threshold*self.stdev_medians
        r_median_high = self.mean_medians + stdev_threshold*self.stdev_medians
        if not (r_median_low <= str_median <= r_median_high):
            return False, str_stats.all_stats, 'median'

        r_std_low = self.mean_stdevs - stdev_threshold*self.stdev_stdevs
        r_std_high = self.mean_stdevs + stdev_threshold*self.stdev_stdevs
        if not (r_std_low <= str_stdev <= r_std_high):
            return False, str_stats.all_stats, 'stdev'

        return True, str_stats.all_stats, None

    def __unicode__(self):
        return self.all_stats


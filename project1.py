from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.compat import jobconf_from_env

class proj1(MRJob):   
    # Fill in your code here

    def mapper(self, _, line):
        station, date, humidity = line.strip().split(',', 2)
        # daily
        yield station + "," + date, (humidity, 1)
        # overall
        yield station + ",9999-99-99", (humidity, 1)

    def combiner(self, key, values):
        total_humidity, counter = 0.0, 0.0

        # sum humidity and get counter
        for i, j in values:
            total_humidity += float(i)
            counter += float(j)
        yield key, (total_humidity, counter)
    
    def reducer_init(self):
        self.tau = int(jobconf_from_env('myjob.settings.tau'))
        self.cur_station = ""
        self.station_avg = 0.0
        # self.daily_avg = 0.0

    def reducer(self, key, values):
        station, date = key.split(',', 1)
        total_humidity, counter = 0.0, 0.0

        # sum humidity and get counter
        for i, j in values:
            total_humidity += float(i)
            counter += float(j)

        if (self.cur_station != station):
            # new station
            self.cur_station = station
            if date == "9999-99-99":
                self.station_avg = total_humidity / counter
            # else:
                # error here
                # TODO: raise exception???
        else:
            # same as previous station
            # self.daily_avg = total_humidity / counter
            daily_avg = total_humidity / counter
            # gap = abs(self.station_avg - self.daily_avg)
            gap = abs(self.station_avg - daily_avg)
            if gap > self.tau:
                # report reading with gap larger than tau
                # yield self.cur_station, f"{date},{gap},{counter},{total_humidity},{self.daily_avg},{self.station_avg}"
                yield self.cur_station, f"{date},{gap}"

    SORT_VALUES = True

    def steps(self):
        JOBCONF = {
            'stream.num.map.output.key.fields': 2,
            'mapreduce.map.output.key.field.separator': ',',
            'mapreduce.job.partitioner': 'org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner',
            'mapreduce.partition.keypartitioner.options':'-k1,1',
            'mapreduce.job.output.key.comparator.class': 'org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator',
            # sort by the station name alphabetically, then by the date in descending order
            'mapreduce.partition.keycomparator.options': '-k1,1 -k2,2r'
        }
        return [MRStep(jobconf = JOBCONF, mapper = self.mapper, combiner = self.combiner, reducer_init = self.reducer_init, reducer = self.reducer)]

if __name__ == '__main__':
    proj1.run()
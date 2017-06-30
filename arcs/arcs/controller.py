import time


class Controller:
    def __init__(self):
        self.collectors = []

    def add_collector(self, collector, frequency):
        """
        Add a new collector to the list of observed objects by the controller.
        
        :param obj collector: A collector object that implement the method required by the controller 
        :param int frequency: How frequent (in seconds) the collector should be run
        :return: 
        """
        self.collectors.append((collector, frequency))

    def run(self):
        while True:
            for collector, frequency in self.collectors:
                collector.collect()
                time.sleep(frequency)

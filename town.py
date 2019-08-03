class Town:
    def __init__(self, name):
        self._name = name
        self._dist = dict()

    def set_dist(self, to_town, dist):
        self._dist[to_town] = dist

    def get_name(self):
        return self._name

    def get_dist(self, to_town):
        return self._dist[to_town]

    def get_dst(self):
        return [town for town in self._dist.keys()]

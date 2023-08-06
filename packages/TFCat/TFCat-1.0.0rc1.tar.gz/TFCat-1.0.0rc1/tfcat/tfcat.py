from tfcat.codec import load, loads
from tfcat.geometry import Polygon, MultiPolygon, Point, MultiPoint, LineString, MultiLineString
from tfcat.feature import Feature
import tfcat.utils
from matplotlib import pyplot as plt
from urllib.request import urlopen


class TFCat:

    def __init__(self, tfcat_data, file_name=None):
        self.file = file_name
        self.data = tfcat_data

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, tfcat_data):
        self._data = tfcat_data

    @property
    def has_observations(self):
        return 'observations' in self._data.keys()

    @property
    def _lookup(self):
        return list(item.properties['obs_id'] for item in self._data.features)

    @classmethod
    def from_file(cls, file_name):
        with open(file_name, 'r') as f:
            tfcat_data = load(f)
        return cls(tfcat_data, file_name=file_name)

    @classmethod
    def from_url(cls, url):
        tfcat_data = loads(urlopen(url).read())
        return cls(tfcat_data, file_name=url)

    @property
    def crs(self):
        return self._data.crs

    @property
    def properties(self):
        return self._data.properties

    @property
    def fields(self):
        return self._data.fields

    def __len__(self):
        return len(self._data.features)

    def observation(self, n):
        return self._data.observations[n]

    def feature(self, n):
        return self._data.features[n]

    @property
    def iter_features(self) -> Feature:
        """
        Generator looping on features
        :return: feature
        """
        n = 0
        while n < len(self):
            yield self.feature(n) #, self.observation(self._lookup[n]) if self.has_observations else None
            n += 1

    @property
    def iter_observations(self) -> Feature:
        """
        Generator looping on observations
        :return: observation
        """
        n = 0
        while n < len(self._data.observations):
            yield self.observation(n)
#            yield [self.feature(i) for i, x in enumerate(self._lookup) if x == n], self.observation(n)
            n += 1

    def iter_features_by_obs_id(self, obs_id: int) -> Feature:
        """
        Generator looping on features within a given obs_id
        :param obs_id: Observation obs_id
        :return: feature
        """
        for i, x in enumerate(self._lookup):
            if x == obs_id:
                yield self.feature(i)

    def _plot_observation(self, oid):

        obs = self.observation(oid)
        crs = self.crs

        bbox_times = [obs.tmin, obs.tmax, obs.tmax, obs.tmin, obs.tmin]
        bbox_times = crs.time_converter(bbox_times).datetime
        bbox_freqs = [obs.fmin, obs.fmin, obs.fmax, obs.fmax, obs.fmin]

        plt.plot(bbox_times, bbox_freqs, '--', label='bbox')

    _plot_style = {
        Point: '+',
        LineString: '-',
        Polygon: '-',
        MultiPoint: '+',
        MultiPolygon: '-',
        MultiLineString: '-',
    }

    def _plot_feature(self, fid):

        feature = self.feature(fid)
        crs = self.crs

        ftype = type(feature.geometry)
        coord = feature['geometry']['coordinates']
        if ftype not in [MultiLineString, MultiPolygon]:
            coord = [coord]
        for item in coord:
            itimes, ifreqs = tfcat.utils.split_coords(item, crs=crs)
            plt.plot(itimes.datetime, ifreqs.value, self._plot_style[ftype], label=f'Feature #{fid}')

    def plot_observation(self, obs_id):

        crs = self.crs

        self._plot_observation(obs_id)

        plt.xlabel(crs.properties['time_coords']['name'])
        plt.ylabel(f"{crs.properties['spectral_coords']['name']} ({crs.properties['spectral_coords']['unit']})")
        plt.title(f'Observation #{obs_id}')

        if obs_id in self._lookup:
            for fid in (i for i, x in enumerate(self._lookup) if x == obs_id):
                self._plot_feature(fid)

        plt.show()

    def plot_feature(self, fid):
        from tfcat.crs import TIME_COORDS

        crs = self.crs
        if crs.type == 'local':
            time_coords = crs.properties.get(
                'time_coords',
                TIME_COORDS[crs.properties['time_coords_id']]
            )
        else:
            raise NotImplemented()

        self._plot_feature(fid)

        plt.xlabel(time_coords['name'])
        plt.ylabel(f"{crs.properties['spectral_coords']['type']} ({crs.properties['spectral_coords']['unit']})")
        plt.title(f'Feature #{fid}')
        plt.show()

    def to_votable(self, file_xml='votable_tfcat.xml'):
        from astropy.io.votable.tree import Param
        from astropy.io.votable import from_table

        votable = from_table(self._data.as_table())
        table = votable.get_first_table()

        for name, value in self.properties.items():
            table.params.append(
                Param(votable, name=name, value=value, arraysize="*", datatype="char")
            )

        votable.to_xml(file_xml)

    def add_property(self, name, field_def, feature_values=None, observation_values=None):

        if not isinstance(field_def, dict):
            raise TypeError('field_def must be a dict')

        self._data.fields[name] = field_def

        if feature_values is not None:
            for feature, value in zip(self._data.features, feature_values):
                feature.properties[name] = value
        if observation_values is not None:
            for observation, value in zip(self._data.observations, observation_values):
                observation.properties[name] = value

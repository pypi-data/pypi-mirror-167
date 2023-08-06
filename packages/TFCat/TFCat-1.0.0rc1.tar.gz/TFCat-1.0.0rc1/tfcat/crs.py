from tfcat.base import Base
from astropy.time import Time
from astropy.units import Unit


class CRS(Base):

    def __init__(self, crs=None, type="local", properties=None, **extra):
        super(CRS).__init__(**extra)
        if crs is not None:
            self['type'] = crs['type']
            self['properties'] = crs['properties']
        if properties is not None:
            self['type'] = type
            self['properties'] = properties

    @classmethod
    def configure(
            cls,
            spectral_coords_id: str,
            ref_position_id: str,
            time_coords=None,
            time_coords_id=None,
            crs_name=None
    ):
        if time_coords is None and time_coords_id is None:
            raise ValueError("TFCat CRS input parameters error: Either 'time_coords' or 'time_coords_id' must be set.")

        crs = {
            'type': "local",
            'properties': {
                'spectral_coords': SPECTRAL_COORDS[spectral_coords_id],
                'ref_position_id': ref_position_id,
            }
        }
        if crs_name is not None:
            crs["properties"]["name"] = crs_name

        if time_coords_id in time_mapping.keys():
            crs["properties"]["time_coords_id"] = time_coords_id
        else:
            crs["properties"]["time_coords"] = time_coords
        return CRS(crs=crs)

    @property
    def time_converter(self):
        if 'time_coords_id' in self.properties.keys():
            return time_mapping[self.properties['time_coords_id']]
        else:
            return self._custom_time_converter

    @property
    def spectral_converter(self):
        return lambda x: x * Unit(self.properties['spectral_coords']['unit'])

    @property
    def converter(self):
        return lambda x: (self.time_converter(x[0]), self.spectral_converter(x[1]))

    @property
    def _custom_time_converter(self):
        time_coords = self.properties['time_coords']
        time_origin = time_coords['time_origin']
        if 'T' in time_origin:
            time_format = 'isot'
        else:
            time_format = 'iso'
        return lambda t: (
            Time(time_origin, format=time_format, scale=time_coords['time_scale'].lower()) +
            t * Unit(time_coords['unit'])
        )


time_mapping = {
    'unix': lambda t: Time(t, format="unix"),
    'jd': lambda t: Time(t, format='jd'),
    'mjd': lambda t: Time(t, format='mjd'),
    'mjd_cnes': lambda t: Time("1950-01-01T00:00:00.000Z", format='iso') + t * Unit('d'),
    'mjd_nasa': lambda t: Time("1968-05-24T00:00:00.000Z", format='iso') + t * Unit('d'),
    'iso': lambda t: Time(t, format='iso'),
    'cdf_tt2000': lambda t: Time('2000-01-01 00:00:00.000Z', format='iso') + t * Unit('ns')
}

TIME_COORDS = {
    'unix': {
        "name": "Timestamp (Unix Time)",
        "unit": "s",
        "time_origin": "1970-01-01T00:00:00.000Z",
        "time_scale": "UTC"
    },
    'jd': {
        "name": "Julian Day",
        "unit": "d",
        "time_origin": "U",
        "time_scale": "UTC"
    },
    'mjd': {
        "name": "Modified Julian Day",
        "unit": "d",
        "time_origin": "1858-11-17T00:00:00.000Z",
        "time_scale": "UTC"
    },
    'mjd_cnes': {
        "name": "Modified Julian Day (CNES definition)",
        "unit": "d",
        "time_origin": "1950-01-01T00:00:00.000Z",
        "time_scale": "UTC"
    },
    'mjd_nasa': {
        "name": "Modified Julian Day (NASA definition)",
        "unit": "d",
        "time_origin": "1968-05-24T00:00:00.000Z",
        "time_scale": "UTC"
    },
    'cdf_tt2000': {
        "name": "CDF Epoch TT2000",
        "unit": "ns",
        "time_origin": "2000-01-01 00:00:00.000Z",
        "time_scale": "TT"
    }
}

SPECTRAL_COORDS = {
    'Hz': {
        "type": "frequency",
        "unit": "Hz"
    },
    'kHz': {
        "type": "frequency",
        "unit": "kHz"
    },
    'MHz': {
        "type": "frequency",
        "unit": "MHz"
    },
    'm': {
        "type": "wavelength",
        "unit": "m"
    },
    'cm': {
        "type": "wavelength",
        "unit": "cm"
    },
    'mm': {
        "type": "wavelength",
        "unit": "mm"
    },
    'cm-1': {
        "type": "wavenumber",
        "unit": "cm**-1"
    },
    'eV': {
        "type": "energy",
        "unit": "eV"
    },
}

REF_POSITION = [
    'GEOCENTER',
]

DefaultCRS = CRS({
    "type": "local",
    "properties": {
        "time_coords_id": 'unix',
        "spectral_coords": SPECTRAL_COORDS['Hz'],
        "ref_position_id": 'GEOCENTER',
    }
})

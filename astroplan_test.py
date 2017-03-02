from astropy.coordinates import SkyCoord
from astroplan import FixedTarget

coordinates = SkyCoord('19h50m47.6s', '+08d52m12.0s', frame='icrs')
altair = FixedTarget(name='Altair',coord= coordinates)

from astroplan import Observer
observer = Observer.at_site('subaru')

import astropy.units as u
from astropy.coordinates import EarthLocation
from pytz import timezone
from astroplan import Observer

longitude = '-155d28m48.900s'
latitude = '+19d49m42.600s'
elevation = 4163*u.m
location = EarthLocation.from_geodetic(longitude, latitude, elevation)

observer = Observer(name ='Subaru Telescope',
                    location = location,
                    pressure = 0.615*u.bar,
                    relative_humidity = 0.11,
                    temperature = 0 * u.deg_C,
                    timezone= timezone('US/Hawaii'),
                    description= "Subaru Telescope Observatory")


from astropy.time import Time
time = Time(['2015-06-16 06:00:00'])

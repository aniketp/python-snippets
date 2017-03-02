from astroplan import Observer
subaru = Observer.at_site('subaru')

from astropy.coordinates import SkyCoord
from astroplan import FixedTarget as fixed

altair = fixed.from_name('Altair')
vega = fixed.from_name('Vega')
deneb = fixed.from_name('Deneb')

from astropy.time import Time

time = Time('2017-03-2 12:00:00')

import numpy as np
import astropy.units as u

altair_rise = subaru.target_rise_time(time,altair)
altair_set = subaru.target_set_time(time,altair)

vega_rise = subaru.target_rise_time(time,vega)
vega_set = subaru.target_set_time(time,vega)

deneb_rise = subaru.target_rise_time(time,deneb)
deneb_set = subaru.target_set_time(time,deneb)

all_up_start = np.max([altair_rise,vega_rise,deneb_rise])
all_up_end = np.min([altair_set,deneb_set,vega_set])

sunset_tonight = subaru.sun_rise_time(time, which='nearest')
sunrise_tonight = subaru.sun_set_time(time, which='nearest')

start = np.max([sunset_tonight,all_up_start])
end = np.min([sunrise_tonight,all_up_end])

print('start')
print('end')

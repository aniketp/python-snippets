Python 2.7.12+ (default, Sep 17 2016, 12:08:02) 
[GCC 6.2.0 20160914] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from astropy import units as u
>>> from astropy import coordinates as record
>>> coord.SkyCoord(ra=10.68458*u.deg, dec=41.26917*u.deg, frame='icrs')

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    coord.SkyCoord(ra=10.68458*u.deg, dec=41.26917*u.deg, frame='icrs')
NameError: name 'coord' is not defined
>>> record.SkyCoord(ra=10.68458*u.deg, dec=41.26917*u.deg, frame='icrs')
<SkyCoord (ICRS): (ra, dec) in deg
    ( 10.68458,  41.26917)>
>>> from astropy.cosmology import WMAP7
>>> from astropy.table import Table
>>> from astropy.wcs import WCS
>>> from astropy.io import fits as pyfits
>>> from astropy import find_api_page
>>> from astropy.units import Quantity
>>> find_api_page(Quantity)

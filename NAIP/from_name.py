import ee
from ee_plugin import Map

image = ee.Image('USDA/NAIP/DOQQ/m_3712213_sw_10_1_20140613')
Map.setCenter(-122.466123, 37.769833, 17)
Map.addLayer(image, {'bands': ['N', 'R','G']}, 'NAIP')
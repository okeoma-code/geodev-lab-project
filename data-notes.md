# Data Notes

## GRID3 Nigeria LGA Boundaries
## OSM Nigeria LGA Boundaries, extracted via the overpass

- Source: https://data.grid3.org/, https://www.openstreetmap.org/
- Dataset: Nigeria LGA Boundaries (GRID3), Owerri West LGA boundary (OSM)
- Downloaded: 13 September 2026
- Study area: Owerri West LGA, Imo State
- Features: 774 polygons (GRID3), 1 polygon (OSM)
- Geometry: Polygon
- Columns: (GRID3) globalid, uniq_id, timestamp, editor, lganame, lgacode, statename, statecode, source, amapcode. (OSM) osm_id, osm_way_id, name, type, aeroway, amenity, admin_leve, barrier, boundary, building, craft, geologicaal, historic, land_area, landuse, leisure, man-made, military, natural, office, place, shop, sport, tourism,other_tags
- Null values: No columns has Null valueson the GRID3 shapefile while some columns have null values on the osm shapefile such as: boundary, building, craft, geologicaal, historic, land_area, landuse, leisure, man-made, military, natural, office, place, shop, sport, tourism,other_tags
- Coverage: The shapefile from OSM Covers the study area fully and also has a better shape that truly represents the Owerri West LGA boundary, while  the GRID3 shapefile doesn't represnt the shape of the boundary well.
- Notes: The layer was used to identify and define the boundary of Owerri West LGA.


## OSM Roads, extracted via QuickOSM

- Source: https://www.openstreetmap.org/
- Query: highway =* within Owerri West extent
- Downloaded: 13 September 2026
- Features: 2590 lines
- Geometry: LineString
- Columns: full_id, osm_id, highway, vehicle, bicycle_ro, constructi, covered, service, start_date, tractype, motor_vehi, maxspeed_a, maxspeed, horse, foot, bicycle, access, junction, layer, bridge, name_en surface, ref, one_way, name, lanes
- Null values: Several road features have missing name and surface information such as: vehicle, bicycle_ro, constructi, covered, service, start_date, tractype, motor_vehi, maxspeed_a, maxspeed, horse, foot, bicycle, access, junction, layer,bridge, name_en surface, ref, one_way, name, lanes
- Coverage: Roads are well represented, it covers the roads within the Local Government
- Notes: The road network was extracted from OpenStreetMap using the QuickOSM plugin in QGIS.


## GRID3 Nigeria Health Facilities

- Source: https://data.grid3.org/
- Dataset: Nigeria Health Facilities
- Downloaded: 13 September 2026
- Features: 81 points
- Geometry: Point
- Columns: globalid, nhfr_uid, nhfr_facil, country, iso, state, lga, lga_name_d, ward, ward_name_, facility_n, facility_1, ownership, ownership_, facility_1, facility_2, latitude, longitude, geocoordin, last_update
- Null values: No facility has Null value
- Coverage: Health facilities are mapped in the known areas of the Study area, while the rural areas lack mapped Facilities.
- Notes: This layer will be used to assess the accessibility of settlements to health facilities.
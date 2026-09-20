# DATA PREPARATION
## STUDY AREA
Owerri West L.G.A, Imo State, Nigeria

## COORDINATE REFERENCE SYSTEM
The datasets arrived in EPSG: 4326 as the CRS, but were reprojected to EPSG: 32632 (WGS 84/UTM ZONE 32N), which is suitable for the study area and also makes it suitable for area measurement.

### DATA reprojected
The following data were reprojected from EPSG:4326 to EPSG:32632 and saved as a GeoPackage file.
- Owerri West L.G.A boundary
- Roads
- Health facilities

#### DATA CLIPPED 
The study area boundary was used as the overlay to clip the other data (Roads, Health facilities).
The clipped data were overlaid on Google Earth imagery:
- The boundary 
- the roads 
- The health facilities 

##### QUALITY NOTES

# GRID3 Owerri West LGA Boundaries
The clipped boundary aligns well with the satellite iimaery.
## OSM Roads, Owerri West L.G.A 
- COMPLETENESS:  the roads covered up 80% of the roads within the study area.
- CURRENCY: the roads were edited recently(september 2026).
- POSITIONAL: the roads aligns well with the satellite imagery.
- ATTRIBUTE: Only about 10% or less carry a surfcae tag.
- FITNESS: Its adequate for analysis, but can't be used for the tag related question.
### GRID3 Owerri West LGA Health Facilities
- COMPLETENESS:  does not cover all known health facilities within the study area. 
- CURRENCY: the health facilities were edited recently(August 14, 2026).
- POSITIONAL: there were duplication of health facilities.
- ATTRIBUTE: all were properly tagged.
- FITNESS: Its adequate for analysis but will require some corrections with regards to the duplicates.





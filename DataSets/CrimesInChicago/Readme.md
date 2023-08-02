# Classic Search With Hyperspace
This notebook demonstrates the use of Hyperspace engine for classic (keyword and value matching) search. The datase set is taken from [Kaggle](https://www.kaggle.com/datasets/chicago/chicago-crime).

# The Dataset - Crimes In Chicago Dataset
(From Kaggle)
"This dataset reflects reported incidents of crime (with the exception of murders where data exists for each victim) that occurred in the City of Chicago from 2001 to present, minus the most recent seven days. Data is extracted from the Chicago Police Department's CLEAR (Citizen Law Enforcement Analysis and Reporting) system. In order to protect the privacy of crime victims, addresses are shown at the block level only and specific locations are not identified. This data includes unverified reports supplied to the Police Department. The preliminary crime classifications may be changed at a later date based upon additional investigation and there is always the possibility of mechanical or human error. Therefore, the Chicago Police Department does not guarantee (either expressed or implied) the accuracy, completeness, timeliness, or correct sequencing of the information and the information should not be used for comparison purposes over time."

The dataset includes 8 Million documents.

## The dataset fields
1. **Case Number {'type': 'keyword'}** -
The Chicago Police Department RD Number (Records Division Number), which is unique to the incident.
2. **Date {'type': 'date', 'format': 'MM/dd/yyyy hh:mm:ss a'}** - Date when the incident occurred. this is sometimes a best estimate.
3. **Block {'type 'keyword'}** -The partially redacted address where the incident occurred, placing it on the same block as the actual address.
4. **IUCR {'type 'keyword'}** - The Illinois Unifrom Crime Reporting code. This is directly linked to the Primary Type and Description. See the list of IUCR codes at https://data.cityofchicago.org/d/c7ck-438e.
5. **Primary Type {'type 'keyword'}** - The primary description of the IUCR code.
6. **Description {'type 'keyword'}** - The secondary description of the IUCR code, a subcategory of the primary description.
7. **Location Description {'type 'keyword'}** - Description of the location where the incident occurred.
8. **Arrest {'type 'boolean'}** - Indicates whether an arrest was made.
9. **Domestic {'type 'boolean'}** - Indicates whether the incident was domestic-related as defined by the Illinois Domestic Violence Act.
10. **Beat {'type 'integer'}** - Indicates the beat where the incident occurred. A beat is the smallest police geographic area – each beat has a dedicated police beat car. Three to five beats make up a police sector, and three sectors make up a police district. The Chicago Police Department has 22 police districts. See the beats at https://data.cityofchicago.org/d/aerh-rz74.
11. **District {'type 'integer'}** - Indicates the police district where the incident occurred. See the districts at https://data.cityofchicago.org/d/fthy-xz3r.
12. **Ward {'type 'integer'}** - The ward (City Council district) where the incident occurred. See the wards at https://data.cityofchicago.org/d/sp34-6z76.
13. **Community Area {'type 'integer'}** - Indicates the community area where the incident occurred. Chicago has 77 community areas. See the community areas at https://data.cityofchicago.org/d/cauq-8yn6.
14. **FBI Code {'type 'keyword'}** - Indicates the crime classification as outlined in the FBI's National Incident-Based Reporting System (NIBRS). See the Chicago Police Department listing of these classifications at http://gis.chicagopolice.org/clearmap_crime_sums/crime_types.html.
15. **X Coordinate {'type 'integer'}** - The x coordinate of the location where the incident occurred in State Plane Illinois East NAD 1983 projection. This location is shifted from the actual location for partial redaction but falls on the same block.
16. **Y Coordinate {'type 'integer'}** - The y coordinate of the location where the incident occurred in State Plane Illinois East NAD 1983 projection. This location is shifted from the actual location for partial redaction but falls on the same block.
17. **Year {'type 'integer'}** - Year the incident occurred.
18. **Updated On {'type 'date', 'format 'MM/dd/yyyy hh:mm:ss a'}** - Date and time the record was last updated.
19. **Latitude {'type 'float'}** - The latitude of the location where the incident occurred. This location is shifted from the actual location for partial redaction but falls on the same block.
20. **Longitude {'type 'float'}** - The longitude of the location where the incident occurred. This location is shifted from the actual location for partial redaction but falls on the same block.
21. **Location {'type 'geo_point', 'struct_type 'list'}** - The location where the incident occurred in a format that allows for creation of maps and other geographic operations on this data portal. This location is shifted from the actual location for partial redaction but falls on the same block.

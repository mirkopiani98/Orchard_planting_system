# Orchard_planting_system
[![DOI](https://zenodo.org/badge/589582074.svg)](https://zenodo.org/badge/latestdoi/589582074)


This script calculates starting from **input reference points** and desired planting distances as rows and tree's distances, the position of each tree in the orchard. At the end of the process a csv database of trees latitude and longitude locations in WGS84 Datum (epsg 4326) is produced. 

**Before using the code** ensure your Python environment being adapt with:

`pip install pandas`
 
`pip install pyproj` 

### Points reference and related lines
+ **AB line** is intended as the line to which tree rows are parallel;
+ **ROWs ALIGNMENT LINE** is intended as the line from which all the tree rows start;
+ **MAX LON line** is the line of maximum longitude, thus any tree after that line will not be added in the orchard database (`orch_db`);
+ **MAX LAT line** is the line of maximum latitufr, thus any tree above that line will not be added in the `orch_db`.

![orchard_planting_system_lines_points](https://user-images.githubusercontent.com/118398203/212771179-4f726ce4-41a3-4ee9-8154-49a30f4b04e4.png)


### Sample preview of the output database.csv

![image](https://user-images.githubusercontent.com/118398203/212690605-6d9e7495-c2f1-42fe-850f-f17159591044.png)

### Created trees database (trees = points) showed inside a GIS software

![image](https://user-images.githubusercontent.com/118398203/212691872-5cf5243d-27be-4935-a925-dd04cb5c26fe.png)

### Trees over a Google satellite image

![image](https://user-images.githubusercontent.com/118398203/212692168-315c0377-435f-45b3-838a-6f94b2c39961.png)


if you found this code usefull please leave a ⭐ and don't forget to reach me out on LinkedIn: [Mirko Piani](https://www.linkedin.com/in/mirko-piani-7b411a1a2/)


# Citation
If you make use of this program, please cite it as:
* Piani, M. (2023). Orchard_planting_system (Version 1.0.0) [Computer software]. https://doi.org/https://doi.org/10.5281/zenodo.7544041

[![DOI](https://zenodo.org/badge/589582074.svg)](https://zenodo.org/badge/latestdoi/589582074)

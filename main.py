from function import planting_system

# enter required inputs
orch_db_fn = input("Enter the path and filename.csv where to create the database file:\n ")
INTERTREE = float(input("Enter the distance between trees along the row (metres):\n "))
INTERROW = float(input("Enter the distance between the tree rows (metres):\n "))

# points in (latitude, longitude) format
'''
P1 -> P2 = AB line

                                                      x <----- (point 5 - max Longitude) ------------------> x                  
                  (point 1) ______________________ x <---- (point 4)  ----> x ______________________ (point 1)
                           |                     /                           \                     | 
                           |      field         /              OR             \        field       |
                           |                   /                               \                   |
                  (point 2)|__________________/ (point 3)             (point 3) \__________________| (point 2)
                  

P1 = first row start
P2 = first row end
P3 = last row end
P4 = maximum latitude
P5 = maximum longitude
'''
 # gcp_list = [(P1 lat, P1 lon), (P2 lat, P2 lon), (P3 lat, P3 lon), (P4 lat, P4 lon), (P5 lat, P5 lon)]
gcp_list = [(44.765369, 11.757010), (44.764581, 11.757738), (44.765563, 11.759384), (44.768388, 11.762985), (44.769848, 11.761676)]



InRow_bearing, orch_db = planting_system(orch_db_fn, INTERTREE, INTERROW, gcp_list)


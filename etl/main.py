from extract.extract  import read_drinking_fountains_data, read_tree_census_data
from transform.transform import transform_drinking_fountains_data, transform_trees_census_data 
from load.export import exportGeo, minifyJson
import time

def ETE_Fountain():
    f = read_drinking_fountains_data()
    f = transform_drinking_fountains_data(f)
    exportGeo(f,"Fountains")
    minifyJson('assets/Fountains.geojson')
    return 0

def ETE_Tree():
    t = read_tree_census_data()
    t = transform_trees_census_data(t)
    exportGeo(t,"Trees")
    minifyJson('assets/Trees.geojson')
    return 0

def main():
    print("Starting ETL process...")
    start = time.time()
    ETE_Fountain()
    stop = time.time()
    print(f"Execution time: {round(stop - start)} Second(s)")
    ETE_Tree()
    end = time.time()
    print(f"Execution time: {round(end - stop)} Second(s)")
    

if __name__ == "__main__":
    main()

# !ISSUE: Error using tree functions with docker

from extract.extract  import read_drinking_fountains_data, read_tree_census_data
from transform.transform import transform_drinking_fountains_data, transform_trees_census_data 
from load.load import load_data
from load.export import exportGeo
import time
import asyncio


async def test_ETL_Fountain(): 
    fountain = read_drinking_fountains_data()
    fountain = transform_drinking_fountains_data(fountain)
    for i, row in fountain.iterrows():
        fountain['coordinates'] = f'{row['coordinates'].x},{row['coordinates'].y}'
    await load_data('Fountains', fountain)
    return 0

async def test_ETL_Tree():
    tree = read_tree_census_data()
    tree = transform_trees_census_data(tree)
    tree = tree.drop(columns=['geometry'])
    await load_data('Trees', tree)
    return 0

def ETE_Fountain():
    f = read_drinking_fountains_data()
    f = transform_drinking_fountains_data(f)
    exportGeo(f,"Fountains")
    return 0

def ETE_Tree():
    t = read_tree_census_data()
    t = transform_trees_census_data(t)
    exportGeo(t,"Trees")
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

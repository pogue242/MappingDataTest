import json
def exportGeo(df, fileName):
    df.to_file(f"assets/{fileName}.geojson", driver='GeoJSON')

def minifyJson(filePath):
    try:
        with open(filePath, 'r') as file:
            data = json.load(file)

        minified = json.dumps(data, separators=(',',':'))

        with open(filePath, 'w') as output:
            output.write(minified)

    except FileNotFoundError:
        print("file not found")
    except Exception as err:
        print(f"error occured: {err}")
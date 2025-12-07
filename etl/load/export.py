def exportGeo(df, fileName):
    df.to_file(f"assets/{fileName}.geojson", driver='GeoJSON')
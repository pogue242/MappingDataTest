def exportGeo(df, fileName):
    df.to_file(f"{fileName}.geojson", driver='GeoJSON')
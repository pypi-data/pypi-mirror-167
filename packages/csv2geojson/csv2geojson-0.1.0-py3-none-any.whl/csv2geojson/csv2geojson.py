import json
import pandas as pd
import geopandas as gpd


def csv2geojson(
    in_csv,
    out_geojson,
    lat_column="latitude",
    long_column="longitude",
    exclude_columns=[],
    include_columns=[],
):
    df = pd.read_csv(in_csv, encoding="utf-8")

    property_df = df

    if exclude_columns:
        property_df = df.loc[:, ~df.columns.isin(exclude_columns)]

    if include_columns:
        property_df = df.loc[:, df.columns.isin(include_columns)]

    gdf = gpd.GeoDataFrame(
        property_df,
        geometry=gpd.points_from_xy(df[lat_column], df[long_column]),
        crs=4326,
    )

    # drop_id: bool, default: False
    data = json.loads(gdf.to_json())
    with open(out_geojson, "w", encoding="utf8") as f:
        # Minify output json
        f.write(json.dumps(data, ensure_ascii=False, separators=(",", ":")))

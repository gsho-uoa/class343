"""
Verification script for GIS environment setup
University of Auckland - GISCI 343
"""

import sys
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

print("=" * 50)
print("GIS Environment Verification")
print("=" * 50)

# Check Python version
print(f"\n✅ Python version: {sys.version.split()[0]}")

# Check package versions
print(f"✅ pandas version: {pd.__version__}")
print(f"✅ geopandas version: {gpd.__version__}")
print(f"✅ matplotlib version: {plt.matplotlib.__version__}")

# Test GeoPandas functionality
print("\n" + "=" * 50)
print("Testing GeoPandas...")
print("=" * 50)

# Create a sample GeoDataFrame with Auckland and Wellington
cities = gpd.GeoDataFrame({
    'city': ['Auckland', 'Wellington', 'Christchurch'],
    'population': [1657200, 215100, 381500],
    'geometry': [
        Point(174.7633, -36.8485),  # Auckland
        Point(174.7762, -41.2865),  # Wellington
        Point(172.6362, -43.5321)   # Christchurch
    ]
}, crs='EPSG:4326')

print(cities)

print("\n✅ All tests passed! Your GIS environment is ready.")
print("\n" + "=" * 50)

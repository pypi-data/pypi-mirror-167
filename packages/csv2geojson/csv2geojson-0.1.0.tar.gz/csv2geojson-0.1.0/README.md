# csv2geojson

Convert csv to geojson

## Installation

```bash
pip install csv2geojson
```

### Development

```bash
git clone https://github.com/YuChunTsao/csv2geojson.git

cd csv2geojson

pip install -e '.[test]'
```

## CLI usage

```txt
usage: csv2geojson [-h] [-v] [-lat lat] [-long long] [-exclude_columns [column_name ...] | -include_columns [column_name ...]]
                   input output

Convert csv to geojson

positional arguments:
  input                 Input csv file path
  output                Output geojson file path

options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -lat lat              Specify the latitude column in csv (default: latitude)
  -long long            Specify the longitude column in csv (default: longitude)
  -exclude_columns [column_name ...]
                        Exclude columns from geojson properties (default: None)
  -include_columns [column_name ...]
                        Include only these columns in the geojson properties (default: None)
```

# Download all free Springer books from links 

## Sample file `springer_links.txt` contains links need to be downloaded 

```
http://link.springer.com/openurl?genre=book&isbn=978-3-662-44874-8
http://link.springer.com/openurl?genre=book&isbn=978-3-319-13072-9
http://link.springer.com/openurl?genre=book&isbn=978-3-319-47831-9
http://link.springer.com/openurl?genre=book&isbn=978-1-4612-1844-9
```

Links of books can be found in `Free+English+textbooks.xlsx`

## Install requirement packages
```
pip install -r requirements.txt
```

## Usage: `python download.py <sample_file> <output_folder>`
```
python download.py springer_links.txt download
```

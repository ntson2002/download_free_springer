# Download all free Springer books from links 

## Sample file `springer_links.txt` contains links need to be downloaded 

```
http://link.springer.com/openurl?genre=book&isbn=978-0-306-48048-5
http://link.springer.com/openurl?genre=book&isbn=978-0-306-48247-2
http://link.springer.com/openurl?genre=book&isbn=978-0-387-21736-9
```


## Install requirement packages
```
pip install -r requirements.txt
```

## Usage: `python download.py <sample_file> <output_folder>`
```
python download.py springer_links.txt download
```

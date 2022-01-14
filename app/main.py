import argparse

from app import config
from app.es import get_es
from app.parse import parse_row
from app.spreadsheet import load


def main(files, delete_indices):
    for file in files:
        print(f'Import {file} started')
        conf = config.load(file)
        es = get_es(conf)
        for tab in conf['file']['tabs']:
            index = tab['index']
            if delete_indices:
                es.indices.delete(index=index, ignore_unavailable=True)
            rows = load(conf['file']['spreadsheetId'], conf['file']['credentialFile'], tab['name'], tab.get('range'))
            headers = rows.pop(0)
            for row in rows:
                definition = {header: row[idx] if len(row) >= idx + 1 else None for idx, header in enumerate(headers)}
                doc = parse_row(definition)
                es.index(index=index, document=doc)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--delete-indices', dest='delete_indices', action='store_true')
    parser.add_argument('-f', '--file', action='append', help='Configuration file')
    parser.set_defaults(delete_indices=False)
    args = parser.parse_args()
    main(args.file, args.delete_indices)

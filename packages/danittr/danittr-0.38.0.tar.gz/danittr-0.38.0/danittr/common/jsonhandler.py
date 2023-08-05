"""Facility for json related tools."""

from json import load, loads, dump


def load_json(filepath):
    """Return json data from file in filepath.

    filepath
        String representing absolute or relative path of
        json file to be loaded.
    """
    try:
        with open(filepath, mode="r", encoding="utf-8") as f:
            data = load(f)
    except FileNotFoundError as err:
        print("File not found: {}".format(filepath))
        raise err

    return data


def save_json(data, filepath):
    """Save data in filepath as a json file.

    data
        Any json serializable data.
    filepath
        String representing absolute or relative path of
        json file to be loaded.
    """
    has_backup = False

    ### before saving data, retrieve a backup of the file
    ### if it exists
    try:
        with open(filepath, mode="r", encoding="utf-8") as f:
            backup = f.read()
            has_backup = True

    except FileNotFoundError as err:
        if not filepath in str(err):
            raise err

    ### only then try to save
    try:
        with open(filepath, mode="w", encoding="utf-8") as w:
            dump(data, w, ensure_ascii=False, indent=2, sort_keys=True)

    ### if something go wrong, save the backup back
    except Exception as err:

        if has_backup:
            with open(filepath, mode="w", encoding="utf-8") as w:
                w.write(backup)

        raise Exception from err

import csv
import os


def export_result(result_data):
    """Export converted name data to ``data/result.csv``.

    The original implementation expected the ``data`` directory to already
    exist, which caused a ``FileNotFoundError`` when it didn't.  Creating the
    directory on the fly makes the function more robust and allows it to be
    used in a fresh environment without manual setup.
    """

    file_path = os.path.join("data", "result.csv")

    # Ensure the output directory exists before attempting to write the file
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(result_data)

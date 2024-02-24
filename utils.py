from pathlib import Path

def make_skcu_folder():
    documents_path_candidates = [
        Path.home() / 'Documents',
        Path.home() / 'My Documents',
    ]
    for path in documents_path_candidates:
        if path.is_dir():
            skcu_folder = path / 'skcu'
            if not skcu_folder.is_dir():
                skcu_folder.mkdir()
            return skcu_folder
    return None


def create_skcu_folder(documents_folder):
    skcu_folder = documents_folder / 'skcu'
    if not skcu_folder.is_dir():
        skcu_folder.mkdir()
    return skcu_folder

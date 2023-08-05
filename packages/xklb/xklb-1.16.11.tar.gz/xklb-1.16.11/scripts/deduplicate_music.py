import argparse, operator
from copy import deepcopy
from pathlib import Path

import humanize
from rich import print, prompt
from tabulate import tabulate

from xklb import db, utils
from xklb.player import remove_media


def get_duplicates(args):
    query = f"""
    SELECT
        m1.path keep_path
        -- , length(m1.path)-length(REPLACE(m1.path, '/', '')) num_slash
        -- , length(m1.path)-length(REPLACE(m1.path, '.', '')) num_dot
        -- , length(m1.path) len_p
        , m2.path duplicate_path
        , m2.size duplicate_size
    FROM
        media m1
    JOIN media m2 on 1=1
        and m2.path != m1.path
        and m1.duration >= m2.duration - 4
        and m1.duration <= m2.duration + 4
        and m1.title = m2.title
        and m1.artist = m2.artist
        and m1.album = m2.album
    WHERE 1=1
        and m1.is_deleted = 0 and m2.is_deleted = 0
        and m1.audio_count > 0 and m2.audio_count > 0
        and abs(m1.sparseness - 1) < 0.1
        and m1.title != ''
        and m1.artist != ''
        and m1.album != ''
    ORDER BY 1=1
        , length(m1.path)-length(REPLACE(m1.path, '/', '')) desc
        , length(m1.path)-length(REPLACE(m1.path, '.', ''))
        , length(m1.path)
        , m1.size desc
        , m1.time_modified desc
        , m1.time_created desc
        , m1.duration desc
        , m1.path desc
    """

    db_resp = list(args.db.query(query))

    return db_resp


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("database")
    parser.add_argument("--only-soft-delete", action="store_true")
    parser.add_argument("--limit", "-L", "-l", "-queue", "--queue", default=100)
    parser.add_argument("--verbose", "-v", action="count", default=0)
    args = parser.parse_args()
    args.db = db.connect(args)
    return args


def deduplicate_music():
    args = parse_args()
    duplicates = get_duplicates(args)
    duplicates_count = len(duplicates)
    duplicates_size = sum(map(operator.itemgetter("duplicate_size"), duplicates))

    tbl = deepcopy(duplicates)
    tbl = tbl[: int(args.limit)]  # TODO: export to CSV
    tbl = utils.col_resize(tbl, "keep_path", 30)
    tbl = utils.col_resize(tbl, "duplicate_path", 30)
    tbl = utils.col_naturalsize(tbl, "duplicate_size")
    print(tabulate(tbl, tablefmt="fancy_grid", headers="keys", showindex=False))  # type: ignore

    print(f"{duplicates_count} duplicates found (showing {args.limit})")
    print(f"Approx. space savings: {humanize.naturalsize(duplicates_size // 2)}")
    print(
        "Warning! This script assumes that the database is up to date. If you have deleted any files manually, run a rescan (via fsadd) for each folder in your database first!"
    )

    if len(duplicates) > 0 and prompt.Confirm.ask("Delete duplicates?", default=False):
        print("Deleting...")

        deleted = []
        for d in duplicates:
            if d["keep_path"] in deleted:
                continue

            path = d["duplicate_path"]
            if not args.only_soft_delete:
                Path(path).unlink(missing_ok=True)
            remove_media(args, path, quiet=True)
            deleted.append(path)

        print(len(deleted), "deleted")


if __name__ == "__main__":
    deduplicate_music()

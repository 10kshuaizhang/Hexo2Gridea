# -*- coding:utf-8 -*-

import os


HEXO_POST_DIR = "XXX/blog/source/_posts/"
GRIDEA_POST_DIR = "XXX/Gridea/posts/"


def substitute_metadata(source_dir: str, target_dir: str):
    for _, _, file_list in os.walk(source_dir):
        for filename in file_list:
            if not filename.endswith(".md"):
                continue
            source_file = os.path.join(source_dir, filename)
            target_file = os.path.join(target_dir, filename)
            with open(target_file, "wb+") as target, open(source_file, 'rb') as source:
                temp_list = source.read().split(b'\n')
                # 2. read the metadata and replace the hexo metadata with new Gridea metadata
                for i, line in enumerate(temp_list):
                    line = line + b'\n'
                    if i == 1:
                        line = line[:7] + b"'" + line[7:-1] + b"'" + line[-1:]
                    if i == 3:
                        line += (
                            b"published: true\nhideInList: false\nfeature: \nisTop: false\n"
                        )
                    target.write(line)


if __name__ == "__main__":
    substitute_metadata(HEXO_POST_DIR, GRIDEA_POST_DIR)

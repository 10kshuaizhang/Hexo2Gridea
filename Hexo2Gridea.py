# -*- coding:utf-8 -*-

import os


HEXO_POST_DIR = "XXX/blog/source/_posts/"
GRIDEA_POST_DIR = "XXX/Gridea/posts/"


def substitute_metadata():
    g = os.walk(HEXO_POST_DIR)
    for _, _, file_list in g:
        for filename in file_list:
            if not filename.endswith("md"):
                continue
            source_file = os.path.join(HEXO_POST_DIR, filename)
            target_file = os.path.join(GRIDEA_POST_DIR, filename)
            with open(target_file, "wb+") as target:
                with open(source_file, 'rb') as source:
                    temp_list = source.read().split('\n'.encode("utf-8"))
                    # 2. read the metadata and replace the hexo metadata with new Gridea metadata
                    for i in range(len(temp_list)):
                        line = temp_list[i] + '\n'.encode('utf-8')
                        if i == 1:
                            line = line[:7] + "'".encode() + line[7:-1] + "'".encode() + line[-1:]
                        if i == 3:
                            line += "published: true\nhideInList: false\nfeature: \nisTop: false\n".encode()
                        target.write(line)


if __name__ == "__main__":
    substitute_metadata()

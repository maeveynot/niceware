#!/usr/bin/python3

import re
import sys
from collections import defaultdict
from functools import reduce

pronunciations = defaultdict(set)  # word -> set(prs)
homophones = defaultdict(set)  # pr -> set(words)
proper_nouns = set()

try:
    pn_out_path, pr_out_path, hp_out_path = sys.argv[1:]
except ValueError:
    msg = "usage: cat ONTOLEX | {} PN_OUT PR_OUT HP_OUT".format(sys.argv[0])
    print(msg, file=sys.stderr)
    sys.exit(1)

cur_block = {}
cur_block_name = ""
for line in sys.stdin:
    line = line.rstrip()
    if re.match(r"^@prefix", line):
        next
    if re.match(r"^eng:", line):
        cur_block_name = line
        cur_block = {}
    if re.match(r"^\s+\S+\s+\S+", line):
        line = re.sub(r"[;.]$", "", line)
        k, v = line.split(None, 1)
        cur_block[k] = v
    if line == "":
        written_reps, phonetic_reps = [
            [s.strip() for s in cur_block.get(k, "").split(" , ") if s]
            for k in ("ontolex:writtenRep", "ontolex:phoneticRep")
        ]
        if written_reps and phonetic_reps:
            for wr in set(written_reps):
                wmatch = re.fullmatch(r'"(\S*?)"@en', wr)
                if wmatch:
                    folded = re.sub(r"\.$", "", wmatch[1]).casefold()
                    if folded not in pronunciations and len(pronunciations) % 200 == 0:
                        msg = "loading: {} ({})...".format(folded, len(pronunciations))
                        print("\r" + " " * 78 + "\r" + msg + " ", end="", file=sys.stderr)
                    if "__Proper_noun__" in cur_block_name:
                        proper_nouns.add(folded)
                    for pr in set(phonetic_reps):
                        pmatch = re.fullmatch(r'"(.*?)"@en-fonipa', pr)
                        if pmatch:
                            pronunciations[folded].add(pmatch[1])
                            homophones[pmatch[1]].add(folded)
                            if pmatch[1][-1] == "s":
                                homophones[pmatch[1][0:-1]].add(folded)
                            if pmatch[1][-2] == "e":
                                homophones[pmatch[1][0:-2]].add(folded)
        cur_block = {}

print(" done!")
print("outputting proper nouns...", file=sys.stderr)
with open(pn_out_path, "w") as f:
    for pn in sorted(proper_nouns):
        print(pn, file=f)

print("outputting pronunciations...", file=sys.stderr)
with open(pr_out_path, "w") as f:
    for w in sorted(pronunciations.keys()):
        print("{}: {}".format(w, ", ".join(pronunciations[w])), file=f)

print("outputting homophones...", file=sys.stderr)
with open(hp_out_path, "w") as f:
    hs = set()
    # all homophones
    for pr, ws in homophones.items():
        if len(ws) > 1:
            hs.add(" ".join(sorted(ws)))
    ## if you just want to check for homophones with an occurence in the wordlist, use this instead
    # with open(wl_in_path) as i:
    #    for w in i.read.splitlines():
    #        hs = reduce(set.union, (homophones[pr] for pr in pronunciations[w]), set())
    #        if len(hs) > 1:
    #            hs.add(" ".join(sorted(ws)))
    for h in hs:
        print(h, file=f)

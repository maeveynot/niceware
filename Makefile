tmp/en_dbnary_ontolex.ttl.bz2:
	curl -L -o $@ http://kaiko.getalp.org/static/ontolex/latest/en_dbnary_ontolex.ttl.bz2

tmp/homophones.txt: tmp/en_dbnary_ontolex.ttl.bz2
	bzcat $^ | ./ontolex-phonemes.py tmp/proper-nouns.txt tmp/pronunciations.txt tmp/homophones.txt

.PHONY: all
all: tmp/homophones.txt

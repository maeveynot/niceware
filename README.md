# Niceware

WARNING! This is still a prototype. When it is frozen, I will note
the year as the "version number".

> We don't just borrow words; on occasion, English has pursued other
> languages down alleyways to beat them unconscious and rifle their
> pockets for new vocabulary. —James Nicoll

> Language has always been the perfect instrument of empire. —Antonio
> de Nebrija, _Granidtica Castellana_

This is an American English Diceware-style wordlist that I compiled for
[Ubik](https://github.com/maeveynot/ubik). It contains 8,192 words, for
use with 13 bits from a CSPRNG, rather than 7,776 for use with five
6-sided physical dice.

I did this because I found existing wordlists unsatisfactory. I have
attempted to exclude (non-exhaustively):

- Words involving punctuation or non-ASCII characters
- Proper nouns, particularly place names, exonyms, and endonyms
- Words with multiple common spellings, that are likely to be confused
  for a homophone if read over an audio channel, or are simply obscure
  enough that the pronunciation might be unknown
- Words that might be embarrassing, offensive, profane, or simply a
  distraction, particularly to marginalized groups
- Words related to religion, race, sexuality, etc (none of these are
  problematic in and of themselves, but because the list includes many
  adjectives with negative connotations, they could be part of a
  combination of words which is)
- Words which might be considered ableist, triggering, or just generally
  unpleasant. Anything you'd CW, basically. If you wouldn't CW anything,
  this probably isn't the wordlist for you.
- Names of drugs, alcoholic drinks, or foods that are categorically
  never halal, kosher, or vegan

All words are between 3 and 9 characters, inclusive. I have attempted to
limit clusters of words with the same stem. My very subjective heuristic
is how fluently I feel I can hold 6 or 7 adversarially-chosen words from
the list in my head while retyping them.

These criteria are political. I believe that language, in spite of its
role as a site of epistemic violence, allows us to express how we can be
better than we are, and that there are so many apropos words for a list
of this kind that continuing to use indifferently-selected ones simply
because they are common in our society is a deliberate choice.

If you believe politics should be kept out of software and engineering,
it's because your politics are already well-represented in capitalist,
patriarchal society and your feelings are prioritized over the safety of
others.

As a wise woman once said, nothing without intention.

## Tools

Homophones were generated from the DBnary dump of Wiktionary with a
Python script, and reviewed manually. Run `make` to generate the list.

## Credit

This list is not based on any particular list, but in the process of
editing it, I referred to the following (all word counts are
`/^[a-z]*$/` only):

Large lists:

- The frequency statistics for the [New General Service
  List](http://www.newgeneralservicelist.org/) and [New Academic Word
  List](http://www.newgeneralservicelist.org/nawl-new-academic-word-list)
  by Browne, Culligan, and Phillip (2013; 31,223 words; CC-BY-SA-4.0)
- The [English-language Wiktionary](https://en.wiktionary.org/), as
  [packaged in Ontolex format](http://kaiko.getalp.org/about-dbnary/) by
  Giles (2014; 54,617 words as of 2020; CC-BY-SA-3.0)
- The [SCOWL American English list](http://wordlist.aspell.net/) by
  Atkinson (2000 or possibly earlier; 49,705 words through size 35 as of
  2019)
- Both components of the [SecureDrop](https://securedrop.org/)
  [name-generator
  list](https://github.com/freedomofpress/securedrop/tree/stable/securedrop/dictionaries)
  by Budington and contributors (2013; 26,069 words as of 2020; AGPL
  3.0)

Diceware-sized lists:

- The [original Diceware
  list](https://theworld.com/~reinhold/diceware.html) by Reinhold (1995;
  7,411 words; CC-BY-4.0)
- The alternative Beale list distributed by Reinhold (probably also
  1995; 7,322 words)
- The [EFF "large"
  list](https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases)
  (2016; 7,772 words; CC-BY-3.0)
- [Two lists](https://github.com/heartsucker/diceware) by Heartsuyker
  (2016; 8,193 words total; MIT)
- The [current SecureDrop
  list](https://github.com/freedomofpress/securedrop/tree/stable/securedrop/wordlists)
  by [Swartz](http://www.rememberaaronsw.com/) and contributors (2012;
  7,599 words as of 2017; AGPL 3.0)

Smaller lists:

- All components of the [Glitch](https://glitch.com/) ["friendly words"
  name-generator list](https://github.com/glitchdotcom/friendly-words)
  (4,347 words as of 2019; MIT)
- The ["left" (adjectives) component of the Docker name-generator
  list](https://github.com/moby/moby/blob/HEAD/pkg/namesgenerator/names-generator.go)
  (108 words as of 2019; Apache 2.0)
- The
  [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki)
  list by Palatinus and possibly collaborators (2013; 2,048 words)

Using various intersections of these lists as a scoring heuristic was
particularly useful for weeding out unlikely candidates; the overlap
ended up being 48-58% of each of the Diceware-sized lists. The
provenance of many lists is unclear, but the SecureDrop lists are based
on Wordnik and SCOWL 7.1 respectively.

For the seven 12-to-14-bit-sized lists (considering the top 8 kibiwords
of the NGSL frequency data as a list), the breakdown of words by how
many of those lists they appear in is:

- 0: 178
- 1: 1,076
- 2: 1,915
- 3: 1,895
- 4: 1,494
- 5: 1,130
- 6: 556
- 7: 355

The Python script was a personal exercise in applying things I learned
in other projects during paid "10% time" graciously provided by my
employer, Freedom of the Press Foundation (who also manage the
development of SecureDrop).

## Biases

This list was compiled by myself, a white, physically abled, queer,
transgender American woman with a Northeastern accent working in
technology. In addition to the limitations of my cultural perspective,
in which I am immensely privileged and have rarely been made to feel
inferior for my diction or vocabulary, I have had to edit this README
tens of times to dial down pretentious word choices.

I consider the exclusion of any words that are not unambiguously spelled
with only the Unicode code points U+0061 through U+007A to be
problematic because it entirely affects "foreign" loanwords, and am
angry that I had to do it. Unfortunately, even in 2020, the material
conditions of actually existing password systems remain generally
xenophobic and user-hostile in their handling of non-ASCII and even
non-alphabetic ASCII characters.

## License

To the extent that a word list can protected by copyright (which I
sincerely hope is nil), I explicitly dedicate this work to the public
domain. For jurisdictions where this is not possible, or contexts where
all assets distributed with a program must have a standard license, you
have the option to redistribute it under the terms of the ISC license.

## Parting Humor

Here is [a comic strip](https://www.bonequest.com/381) that I have been
quoting for approximately 20 years. I still enjoy this extremely
offensive continuing series of sequential art.

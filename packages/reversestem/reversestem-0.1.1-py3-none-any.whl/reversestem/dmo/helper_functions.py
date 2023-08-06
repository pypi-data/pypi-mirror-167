#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import unicodedata2

from typing import Callable


def text_to_chars(input_text: str) -> str:

    def transform(ch):
        """Checks whether `char` is a punctuation character."""
        if ch.isnumeric():
            return '_'
        cp = ord(ch)
        if (cp >= 33 and cp <= 47) or (cp >= 58 and cp <= 64) or (cp >= 91 and cp <= 96) or (cp >= 123 and cp <= 126):
            return '_'  # is punct
        cat = unicodedata2.category(ch)
        if cat.startswith("P"):
            return '_'  # is punct
        return ch  # not punct

    input_text = [transform(ch) for ch in input_text]

    return input_text


def unstem_input(input_text: str,
                 d_trie_finder: Callable,
                 flatten: bool = False) -> dict or list or None:

    input_text = input_text.lower().replace(' ', '_')
    chars = text_to_chars(input_text[:2])

    d_trie = d_trie_finder(''.join(chars[:2]))
    if not d_trie:
        return None
    if input_text not in d_trie:
        return None

    d_result = d_trie[input_text]

    if not flatten:
        return d_result

    s = set()
    for k in d_result:
        s.add(k)
        [s.add(x) for x in d_result[k]]

    return sorted(s, key=len, reverse=True)

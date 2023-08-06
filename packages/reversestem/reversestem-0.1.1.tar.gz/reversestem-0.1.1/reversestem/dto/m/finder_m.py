
#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from functools import lru_cache

from reversestem.dmo import unstem_input


# AUTO GENERATED FINDER
class FinderM(object):

    def _get_trie(self,
                  ftc: str) -> dict:

        if ftc == 'm_':
            from reversestem.dto.m import d_stem_m_
            return d_stem_m_

        if ftc == 'ma':
            from reversestem.dto.m import d_stem_ma
            return d_stem_ma

        if ftc == 'mb':
            from reversestem.dto.m import d_stem_mb
            return d_stem_mb

        if ftc == 'mc':
            from reversestem.dto.m import d_stem_mc
            return d_stem_mc

        if ftc == 'md':
            from reversestem.dto.m import d_stem_md
            return d_stem_md

        if ftc == 'me':
            from reversestem.dto.m import d_stem_me
            return d_stem_me

        if ftc == 'mf':
            from reversestem.dto.m import d_stem_mf
            return d_stem_mf

        if ftc == 'mg':
            from reversestem.dto.m import d_stem_mg
            return d_stem_mg

        if ftc == 'mh':
            from reversestem.dto.m import d_stem_mh
            return d_stem_mh

        if ftc == 'mi':
            from reversestem.dto.m import d_stem_mi
            return d_stem_mi

        if ftc == 'mj':
            from reversestem.dto.m import d_stem_mj
            return d_stem_mj

        if ftc == 'mk':
            from reversestem.dto.m import d_stem_mk
            return d_stem_mk

        if ftc == 'ml':
            from reversestem.dto.m import d_stem_ml
            return d_stem_ml

        if ftc == 'mm':
            from reversestem.dto.m import d_stem_mm
            return d_stem_mm

        if ftc == 'mn':
            from reversestem.dto.m import d_stem_mn
            return d_stem_mn

        if ftc == 'mo':
            from reversestem.dto.m import d_stem_mo
            return d_stem_mo

        if ftc == 'mp':
            from reversestem.dto.m import d_stem_mp
            return d_stem_mp

        if ftc == 'mq':
            from reversestem.dto.m import d_stem_mq
            return d_stem_mq

        if ftc == 'mr':
            from reversestem.dto.m import d_stem_mr
            return d_stem_mr

        if ftc == 'ms':
            from reversestem.dto.m import d_stem_ms
            return d_stem_ms

        if ftc == 'mt':
            from reversestem.dto.m import d_stem_mt
            return d_stem_mt

        if ftc == 'mu':
            from reversestem.dto.m import d_stem_mu
            return d_stem_mu

        if ftc == 'mv':
            from reversestem.dto.m import d_stem_mv
            return d_stem_mv

        if ftc == 'mw':
            from reversestem.dto.m import d_stem_mw
            return d_stem_mw

        if ftc == 'my':
            from reversestem.dto.m import d_stem_my
            return d_stem_my

        if ftc == 'mz':
            from reversestem.dto.m import d_stem_mz
            return d_stem_mz

    @lru_cache(maxsize=1024)
    def unstem(self,
               input_text: str,
               flatten: bool = False) -> dict or list or None:
        input_text = input_text.lower().replace(' ', '_')
        return unstem_input(input_text=input_text,
                            d_trie_finder=self._get_trie,
                            flatten=flatten)


#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from reversestem.dmo import unstem_input


# AUTO GENERATED FINDER
class FinderA(object):

    def _get_trie(self,
                  ftc: str) -> dict:

        if ftc == 'a_':
            from reversestem.dto.a import d_stem_a_
            return d_stem_a_

        if ftc == 'aa':
            from reversestem.dto.a import d_stem_aa
            return d_stem_aa

        if ftc == 'ab':
            from reversestem.dto.a import d_stem_ab
            return d_stem_ab

        if ftc == 'ac':
            from reversestem.dto.a import d_stem_ac
            return d_stem_ac

        if ftc == 'ad':
            from reversestem.dto.a import d_stem_ad
            return d_stem_ad

        if ftc == 'ae':
            from reversestem.dto.a import d_stem_ae
            return d_stem_ae

        if ftc == 'af':
            from reversestem.dto.a import d_stem_af
            return d_stem_af

        if ftc == 'ag':
            from reversestem.dto.a import d_stem_ag
            return d_stem_ag

        if ftc == 'ah':
            from reversestem.dto.a import d_stem_ah
            return d_stem_ah

        if ftc == 'ai':
            from reversestem.dto.a import d_stem_ai
            return d_stem_ai

        if ftc == 'aj':
            from reversestem.dto.a import d_stem_aj
            return d_stem_aj

        if ftc == 'ak':
            from reversestem.dto.a import d_stem_ak
            return d_stem_ak

        if ftc == 'al':
            from reversestem.dto.a import d_stem_al
            return d_stem_al

        if ftc == 'am':
            from reversestem.dto.a import d_stem_am
            return d_stem_am

        if ftc == 'an':
            from reversestem.dto.a import d_stem_an
            return d_stem_an

        if ftc == 'ao':
            from reversestem.dto.a import d_stem_ao
            return d_stem_ao

        if ftc == 'ap':
            from reversestem.dto.a import d_stem_ap
            return d_stem_ap

        if ftc == 'aq':
            from reversestem.dto.a import d_stem_aq
            return d_stem_aq

        if ftc == 'ar':
            from reversestem.dto.a import d_stem_ar
            return d_stem_ar

        if ftc == 'as':
            from reversestem.dto.a import d_stem_as
            return d_stem_as

        if ftc == 'at':
            from reversestem.dto.a import d_stem_at
            return d_stem_at

        if ftc == 'au':
            from reversestem.dto.a import d_stem_au
            return d_stem_au

        if ftc == 'av':
            from reversestem.dto.a import d_stem_av
            return d_stem_av

        if ftc == 'aw':
            from reversestem.dto.a import d_stem_aw
            return d_stem_aw

        if ftc == 'ay':
            from reversestem.dto.a import d_stem_ay
            return d_stem_ay

        if ftc == 'az':
            from reversestem.dto.a import d_stem_az
            return d_stem_az

    def unstem(self,
               input_text: str,
               flatten: bool = False) -> dict or list or None:
        input_text = input_text.lower().replace(' ', '_')
        return unstem_input(input_text=input_text,
                            d_trie_finder=self._get_trie,
                            flatten=flatten)

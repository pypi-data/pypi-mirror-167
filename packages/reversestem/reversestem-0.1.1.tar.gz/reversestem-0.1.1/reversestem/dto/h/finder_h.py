
#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from reversestem.dmo import unstem_input


# AUTO GENERATED FINDER
class FinderH(object):

    def _get_trie(self,
                  ftc: str) -> dict:

        
        if ftc == 'h_':
            from reversestem.dto.h import d_stem_h_
            return d_stem_h_        
        

        if ftc == 'ha':
            from reversestem.dto.h import d_stem_ha
            return d_stem_ha        
        

        if ftc == 'hb':
            from reversestem.dto.h import d_stem_hb
            return d_stem_hb        
        

        if ftc == 'hc':
            from reversestem.dto.h import d_stem_hc
            return d_stem_hc        
        

        if ftc == 'hd':
            from reversestem.dto.h import d_stem_hd
            return d_stem_hd        
        

        if ftc == 'he':
            from reversestem.dto.h import d_stem_he
            return d_stem_he        
        

        if ftc == 'hf':
            from reversestem.dto.h import d_stem_hf
            return d_stem_hf        
        

        if ftc == 'hg':
            from reversestem.dto.h import d_stem_hg
            return d_stem_hg        
        

        if ftc == 'hh':
            from reversestem.dto.h import d_stem_hh
            return d_stem_hh        
        

        if ftc == 'hi':
            from reversestem.dto.h import d_stem_hi
            return d_stem_hi        
        

        if ftc == 'hj':
            from reversestem.dto.h import d_stem_hj
            return d_stem_hj        
        

        if ftc == 'hk':
            from reversestem.dto.h import d_stem_hk
            return d_stem_hk        
        

        if ftc == 'hl':
            from reversestem.dto.h import d_stem_hl
            return d_stem_hl        
        

        if ftc == 'hm':
            from reversestem.dto.h import d_stem_hm
            return d_stem_hm        
        

        if ftc == 'hn':
            from reversestem.dto.h import d_stem_hn
            return d_stem_hn        
        

        if ftc == 'ho':
            from reversestem.dto.h import d_stem_ho
            return d_stem_ho        
        

        if ftc == 'hp':
            from reversestem.dto.h import d_stem_hp
            return d_stem_hp        
        

        if ftc == 'hq':
            from reversestem.dto.h import d_stem_hq
            return d_stem_hq        
        

        if ftc == 'hr':
            from reversestem.dto.h import d_stem_hr
            return d_stem_hr        
        

        if ftc == 'hs':
            from reversestem.dto.h import d_stem_hs
            return d_stem_hs        
        

        if ftc == 'ht':
            from reversestem.dto.h import d_stem_ht
            return d_stem_ht        
        

        if ftc == 'hu':
            from reversestem.dto.h import d_stem_hu
            return d_stem_hu        
        

        if ftc == 'hv':
            from reversestem.dto.h import d_stem_hv
            return d_stem_hv        
        

        if ftc == 'hw':
            from reversestem.dto.h import d_stem_hw
            return d_stem_hw        
        

        if ftc == 'hy':
            from reversestem.dto.h import d_stem_hy
            return d_stem_hy        
        

        if ftc == 'hz':
            from reversestem.dto.h import d_stem_hz
            return d_stem_hz        
        

    def unstem(self,
               input_text: str,
               flatten: bool = False) -> dict or list or None:
        input_text = input_text.lower().replace(' ', '_')
        return unstem_input(input_text=input_text,
                            d_trie_finder=self._get_trie,
                            flatten=flatten)
        
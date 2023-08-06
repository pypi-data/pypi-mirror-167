
#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from reversestem.dmo import unstem_input


# AUTO GENERATED FINDER
class FinderC(object):

    def _get_trie(self,
                  ftc: str) -> dict:

        
        if ftc == 'c_':
            from reversestem.dto.c import d_stem_c_
            return d_stem_c_        
        

        if ftc == 'ca':
            from reversestem.dto.c import d_stem_ca
            return d_stem_ca        
        

        if ftc == 'cb':
            from reversestem.dto.c import d_stem_cb
            return d_stem_cb        
        

        if ftc == 'cc':
            from reversestem.dto.c import d_stem_cc
            return d_stem_cc        
        

        if ftc == 'cd':
            from reversestem.dto.c import d_stem_cd
            return d_stem_cd        
        

        if ftc == 'ce':
            from reversestem.dto.c import d_stem_ce
            return d_stem_ce        
        

        if ftc == 'cf':
            from reversestem.dto.c import d_stem_cf
            return d_stem_cf        
        

        if ftc == 'cg':
            from reversestem.dto.c import d_stem_cg
            return d_stem_cg        
        

        if ftc == 'ch':
            from reversestem.dto.c import d_stem_ch
            return d_stem_ch        
        

        if ftc == 'ci':
            from reversestem.dto.c import d_stem_ci
            return d_stem_ci        
        

        if ftc == 'cj':
            from reversestem.dto.c import d_stem_cj
            return d_stem_cj        
        

        if ftc == 'ck':
            from reversestem.dto.c import d_stem_ck
            return d_stem_ck        
        

        if ftc == 'cl':
            from reversestem.dto.c import d_stem_cl
            return d_stem_cl        
        

        if ftc == 'cm':
            from reversestem.dto.c import d_stem_cm
            return d_stem_cm        
        

        if ftc == 'cn':
            from reversestem.dto.c import d_stem_cn
            return d_stem_cn        
        

        if ftc == 'co':
            from reversestem.dto.c import d_stem_co
            return d_stem_co        
        

        if ftc == 'cp':
            from reversestem.dto.c import d_stem_cp
            return d_stem_cp        
        

        if ftc == 'cq':
            from reversestem.dto.c import d_stem_cq
            return d_stem_cq        
        

        if ftc == 'cr':
            from reversestem.dto.c import d_stem_cr
            return d_stem_cr        
        

        if ftc == 'cs':
            from reversestem.dto.c import d_stem_cs
            return d_stem_cs        
        

        if ftc == 'ct':
            from reversestem.dto.c import d_stem_ct
            return d_stem_ct        
        

        if ftc == 'cu':
            from reversestem.dto.c import d_stem_cu
            return d_stem_cu        
        

        if ftc == 'cv':
            from reversestem.dto.c import d_stem_cv
            return d_stem_cv        
        

        if ftc == 'cw':
            from reversestem.dto.c import d_stem_cw
            return d_stem_cw        
        

        if ftc == 'cy':
            from reversestem.dto.c import d_stem_cy
            return d_stem_cy        
        

        if ftc == 'cz':
            from reversestem.dto.c import d_stem_cz
            return d_stem_cz        
        

    def unstem(self,
               input_text: str,
               flatten: bool = False) -> dict or list or None:
        input_text = input_text.lower().replace(' ', '_')
        return unstem_input(input_text=input_text,
                            d_trie_finder=self._get_trie,
                            flatten=flatten)
        
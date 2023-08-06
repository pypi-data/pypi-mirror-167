
#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from reversestem.dmo import unstem_input


# AUTO GENERATED FINDER
class FinderS(object):

    def _get_trie(self,
                  ftc: str) -> dict:

        
        if ftc == 's_':
            from reversestem.dto.s import d_stem_s_
            return d_stem_s_        
        

        if ftc == 'sa':
            from reversestem.dto.s import d_stem_sa
            return d_stem_sa        
        

        if ftc == 'sb':
            from reversestem.dto.s import d_stem_sb
            return d_stem_sb        
        

        if ftc == 'sc':
            from reversestem.dto.s import d_stem_sc
            return d_stem_sc        
        

        if ftc == 'sd':
            from reversestem.dto.s import d_stem_sd
            return d_stem_sd        
        

        if ftc == 'se':
            from reversestem.dto.s import d_stem_se
            return d_stem_se        
        

        if ftc == 'sf':
            from reversestem.dto.s import d_stem_sf
            return d_stem_sf        
        

        if ftc == 'sg':
            from reversestem.dto.s import d_stem_sg
            return d_stem_sg        
        

        if ftc == 'sh':
            from reversestem.dto.s import d_stem_sh
            return d_stem_sh        
        

        if ftc == 'si':
            from reversestem.dto.s import d_stem_si
            return d_stem_si        
        

        if ftc == 'sj':
            from reversestem.dto.s import d_stem_sj
            return d_stem_sj        
        

        if ftc == 'sk':
            from reversestem.dto.s import d_stem_sk
            return d_stem_sk        
        

        if ftc == 'sl':
            from reversestem.dto.s import d_stem_sl
            return d_stem_sl        
        

        if ftc == 'sm':
            from reversestem.dto.s import d_stem_sm
            return d_stem_sm        
        

        if ftc == 'sn':
            from reversestem.dto.s import d_stem_sn
            return d_stem_sn        
        

        if ftc == 'so':
            from reversestem.dto.s import d_stem_so
            return d_stem_so        
        

        if ftc == 'sp':
            from reversestem.dto.s import d_stem_sp
            return d_stem_sp        
        

        if ftc == 'sq':
            from reversestem.dto.s import d_stem_sq
            return d_stem_sq        
        

        if ftc == 'sr':
            from reversestem.dto.s import d_stem_sr
            return d_stem_sr        
        

        if ftc == 'ss':
            from reversestem.dto.s import d_stem_ss
            return d_stem_ss        
        

        if ftc == 'st':
            from reversestem.dto.s import d_stem_st
            return d_stem_st        
        

        if ftc == 'su':
            from reversestem.dto.s import d_stem_su
            return d_stem_su        
        

        if ftc == 'sv':
            from reversestem.dto.s import d_stem_sv
            return d_stem_sv        
        

        if ftc == 'sw':
            from reversestem.dto.s import d_stem_sw
            return d_stem_sw        
        

        if ftc == 'sy':
            from reversestem.dto.s import d_stem_sy
            return d_stem_sy        
        

        if ftc == 'sz':
            from reversestem.dto.s import d_stem_sz
            return d_stem_sz        
        

    def unstem(self,
               input_text: str,
               flatten: bool = False) -> dict or list or None:
        input_text = input_text.lower().replace(' ', '_')
        return unstem_input(input_text=input_text,
                            d_trie_finder=self._get_trie,
                            flatten=flatten)
        
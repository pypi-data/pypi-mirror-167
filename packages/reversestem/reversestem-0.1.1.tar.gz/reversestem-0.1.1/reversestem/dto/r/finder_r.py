
#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from reversestem.dmo import unstem_input


# AUTO GENERATED FINDER
class FinderR(object):

    def _get_trie(self,
                  ftc: str) -> dict:

        
        if ftc == 'r_':
            from reversestem.dto.r import d_stem_r_
            return d_stem_r_        
        

        if ftc == 'ra':
            from reversestem.dto.r import d_stem_ra
            return d_stem_ra        
        

        if ftc == 'rb':
            from reversestem.dto.r import d_stem_rb
            return d_stem_rb        
        

        if ftc == 'rc':
            from reversestem.dto.r import d_stem_rc
            return d_stem_rc        
        

        if ftc == 'rd':
            from reversestem.dto.r import d_stem_rd
            return d_stem_rd        
        

        if ftc == 're':
            from reversestem.dto.r import d_stem_re
            return d_stem_re        
        

        if ftc == 'rf':
            from reversestem.dto.r import d_stem_rf
            return d_stem_rf        
        

        if ftc == 'rg':
            from reversestem.dto.r import d_stem_rg
            return d_stem_rg        
        

        if ftc == 'rh':
            from reversestem.dto.r import d_stem_rh
            return d_stem_rh        
        

        if ftc == 'ri':
            from reversestem.dto.r import d_stem_ri
            return d_stem_ri        
        

        if ftc == 'rj':
            from reversestem.dto.r import d_stem_rj
            return d_stem_rj        
        

        if ftc == 'rk':
            from reversestem.dto.r import d_stem_rk
            return d_stem_rk        
        

        if ftc == 'rl':
            from reversestem.dto.r import d_stem_rl
            return d_stem_rl        
        

        if ftc == 'rm':
            from reversestem.dto.r import d_stem_rm
            return d_stem_rm        
        

        if ftc == 'rn':
            from reversestem.dto.r import d_stem_rn
            return d_stem_rn        
        

        if ftc == 'ro':
            from reversestem.dto.r import d_stem_ro
            return d_stem_ro        
        

        if ftc == 'rp':
            from reversestem.dto.r import d_stem_rp
            return d_stem_rp        
        

        if ftc == 'rq':
            from reversestem.dto.r import d_stem_rq
            return d_stem_rq        
        

        if ftc == 'rr':
            from reversestem.dto.r import d_stem_rr
            return d_stem_rr        
        

        if ftc == 'rs':
            from reversestem.dto.r import d_stem_rs
            return d_stem_rs        
        

        if ftc == 'rt':
            from reversestem.dto.r import d_stem_rt
            return d_stem_rt        
        

        if ftc == 'ru':
            from reversestem.dto.r import d_stem_ru
            return d_stem_ru        
        

        if ftc == 'rv':
            from reversestem.dto.r import d_stem_rv
            return d_stem_rv        
        

        if ftc == 'rw':
            from reversestem.dto.r import d_stem_rw
            return d_stem_rw        
        

        if ftc == 'ry':
            from reversestem.dto.r import d_stem_ry
            return d_stem_ry        
        

        if ftc == 'rz':
            from reversestem.dto.r import d_stem_rz
            return d_stem_rz        
        

    def unstem(self,
               input_text: str,
               flatten: bool = False) -> dict or list or None:
        input_text = input_text.lower().replace(' ', '_')
        return unstem_input(input_text=input_text,
                            d_trie_finder=self._get_trie,
                            flatten=flatten)
        
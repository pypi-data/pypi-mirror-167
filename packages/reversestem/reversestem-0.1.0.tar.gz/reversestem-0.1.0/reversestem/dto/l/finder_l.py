
#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from reversestem.dmo import unstem_input


# AUTO GENERATED FINDER
class FinderL(object):

    def _get_trie(self,
                  ftc: str) -> dict:

        
        if ftc == 'l_':
            from reversestem.dto.l import d_stem_l_
            return d_stem_l_        
        

        if ftc == 'la':
            from reversestem.dto.l import d_stem_la
            return d_stem_la        
        

        if ftc == 'lb':
            from reversestem.dto.l import d_stem_lb
            return d_stem_lb        
        

        if ftc == 'lc':
            from reversestem.dto.l import d_stem_lc
            return d_stem_lc        
        

        if ftc == 'ld':
            from reversestem.dto.l import d_stem_ld
            return d_stem_ld        
        

        if ftc == 'le':
            from reversestem.dto.l import d_stem_le
            return d_stem_le        
        

        if ftc == 'lf':
            from reversestem.dto.l import d_stem_lf
            return d_stem_lf        
        

        if ftc == 'lg':
            from reversestem.dto.l import d_stem_lg
            return d_stem_lg        
        

        if ftc == 'lh':
            from reversestem.dto.l import d_stem_lh
            return d_stem_lh        
        

        if ftc == 'li':
            from reversestem.dto.l import d_stem_li
            return d_stem_li        
        

        if ftc == 'lj':
            from reversestem.dto.l import d_stem_lj
            return d_stem_lj        
        

        if ftc == 'lk':
            from reversestem.dto.l import d_stem_lk
            return d_stem_lk        
        

        if ftc == 'll':
            from reversestem.dto.l import d_stem_ll
            return d_stem_ll        
        

        if ftc == 'lm':
            from reversestem.dto.l import d_stem_lm
            return d_stem_lm        
        

        if ftc == 'ln':
            from reversestem.dto.l import d_stem_ln
            return d_stem_ln        
        

        if ftc == 'lo':
            from reversestem.dto.l import d_stem_lo
            return d_stem_lo        
        

        if ftc == 'lp':
            from reversestem.dto.l import d_stem_lp
            return d_stem_lp        
        

        if ftc == 'lq':
            from reversestem.dto.l import d_stem_lq
            return d_stem_lq        
        

        if ftc == 'lr':
            from reversestem.dto.l import d_stem_lr
            return d_stem_lr        
        

        if ftc == 'ls':
            from reversestem.dto.l import d_stem_ls
            return d_stem_ls        
        

        if ftc == 'lt':
            from reversestem.dto.l import d_stem_lt
            return d_stem_lt        
        

        if ftc == 'lu':
            from reversestem.dto.l import d_stem_lu
            return d_stem_lu        
        

        if ftc == 'lv':
            from reversestem.dto.l import d_stem_lv
            return d_stem_lv        
        

        if ftc == 'lw':
            from reversestem.dto.l import d_stem_lw
            return d_stem_lw        
        

        if ftc == 'ly':
            from reversestem.dto.l import d_stem_ly
            return d_stem_ly        
        

        if ftc == 'lz':
            from reversestem.dto.l import d_stem_lz
            return d_stem_lz        
        

    def unstem(self,
               input_text: str,
               flatten: bool = False) -> dict or list or None:
        input_text = input_text.lower().replace(' ', '_')
        return unstem_input(input_text=input_text,
                            d_trie_finder=self._get_trie,
                            flatten=flatten)
        
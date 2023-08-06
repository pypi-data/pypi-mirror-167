
#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from reversestem.dmo import unstem_input


# AUTO GENERATED FINDER
class FinderF(object):

    def _get_trie(self,
                  ftc: str) -> dict:

        
        if ftc == 'f_':
            from reversestem.dto.f import d_stem_f_
            return d_stem_f_        
        

        if ftc == 'fa':
            from reversestem.dto.f import d_stem_fa
            return d_stem_fa        
        

        if ftc == 'fb':
            from reversestem.dto.f import d_stem_fb
            return d_stem_fb        
        

        if ftc == 'fc':
            from reversestem.dto.f import d_stem_fc
            return d_stem_fc        
        

        if ftc == 'fd':
            from reversestem.dto.f import d_stem_fd
            return d_stem_fd        
        

        if ftc == 'fe':
            from reversestem.dto.f import d_stem_fe
            return d_stem_fe        
        

        if ftc == 'ff':
            from reversestem.dto.f import d_stem_ff
            return d_stem_ff        
        

        if ftc == 'fg':
            from reversestem.dto.f import d_stem_fg
            return d_stem_fg        
        

        if ftc == 'fh':
            from reversestem.dto.f import d_stem_fh
            return d_stem_fh        
        

        if ftc == 'fi':
            from reversestem.dto.f import d_stem_fi
            return d_stem_fi        
        

        if ftc == 'fj':
            from reversestem.dto.f import d_stem_fj
            return d_stem_fj        
        

        if ftc == 'fk':
            from reversestem.dto.f import d_stem_fk
            return d_stem_fk        
        

        if ftc == 'fl':
            from reversestem.dto.f import d_stem_fl
            return d_stem_fl        
        

        if ftc == 'fm':
            from reversestem.dto.f import d_stem_fm
            return d_stem_fm        
        

        if ftc == 'fn':
            from reversestem.dto.f import d_stem_fn
            return d_stem_fn        
        

        if ftc == 'fo':
            from reversestem.dto.f import d_stem_fo
            return d_stem_fo        
        

        if ftc == 'fp':
            from reversestem.dto.f import d_stem_fp
            return d_stem_fp        
        

        if ftc == 'fq':
            from reversestem.dto.f import d_stem_fq
            return d_stem_fq        
        

        if ftc == 'fr':
            from reversestem.dto.f import d_stem_fr
            return d_stem_fr        
        

        if ftc == 'fs':
            from reversestem.dto.f import d_stem_fs
            return d_stem_fs        
        

        if ftc == 'ft':
            from reversestem.dto.f import d_stem_ft
            return d_stem_ft        
        

        if ftc == 'fu':
            from reversestem.dto.f import d_stem_fu
            return d_stem_fu        
        

        if ftc == 'fv':
            from reversestem.dto.f import d_stem_fv
            return d_stem_fv        
        

        if ftc == 'fw':
            from reversestem.dto.f import d_stem_fw
            return d_stem_fw        
        

        if ftc == 'fy':
            from reversestem.dto.f import d_stem_fy
            return d_stem_fy        
        

        if ftc == 'fz':
            from reversestem.dto.f import d_stem_fz
            return d_stem_fz        
        

    def unstem(self,
               input_text: str,
               flatten: bool = False) -> dict or list or None:
        input_text = input_text.lower().replace(' ', '_')
        return unstem_input(input_text=input_text,
                            d_trie_finder=self._get_trie,
                            flatten=flatten)
        
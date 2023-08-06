
#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from reversestem.dmo import unstem_input


# AUTO GENERATED FINDER
class FinderU(object):

    def _get_trie(self,
                  ftc: str) -> dict:

        
        if ftc == 'u_':
            from reversestem.dto.u import d_stem_u_
            return d_stem_u_        
        

        if ftc == 'ua':
            from reversestem.dto.u import d_stem_ua
            return d_stem_ua        
        

        if ftc == 'ub':
            from reversestem.dto.u import d_stem_ub
            return d_stem_ub        
        

        if ftc == 'uc':
            from reversestem.dto.u import d_stem_uc
            return d_stem_uc        
        

        if ftc == 'ud':
            from reversestem.dto.u import d_stem_ud
            return d_stem_ud        
        

        if ftc == 'ue':
            from reversestem.dto.u import d_stem_ue
            return d_stem_ue        
        

        if ftc == 'uf':
            from reversestem.dto.u import d_stem_uf
            return d_stem_uf        
        

        if ftc == 'ug':
            from reversestem.dto.u import d_stem_ug
            return d_stem_ug        
        

        if ftc == 'uh':
            from reversestem.dto.u import d_stem_uh
            return d_stem_uh        
        

        if ftc == 'ui':
            from reversestem.dto.u import d_stem_ui
            return d_stem_ui        
        

        if ftc == 'uj':
            from reversestem.dto.u import d_stem_uj
            return d_stem_uj        
        

        if ftc == 'uk':
            from reversestem.dto.u import d_stem_uk
            return d_stem_uk        
        

        if ftc == 'ul':
            from reversestem.dto.u import d_stem_ul
            return d_stem_ul        
        

        if ftc == 'um':
            from reversestem.dto.u import d_stem_um
            return d_stem_um        
        

        if ftc == 'un':
            from reversestem.dto.u import d_stem_un
            return d_stem_un        
        

        if ftc == 'uo':
            from reversestem.dto.u import d_stem_uo
            return d_stem_uo        
        

        if ftc == 'up':
            from reversestem.dto.u import d_stem_up
            return d_stem_up        
        

        if ftc == 'uq':
            from reversestem.dto.u import d_stem_uq
            return d_stem_uq        
        

        if ftc == 'ur':
            from reversestem.dto.u import d_stem_ur
            return d_stem_ur        
        

        if ftc == 'us':
            from reversestem.dto.u import d_stem_us
            return d_stem_us        
        

        if ftc == 'ut':
            from reversestem.dto.u import d_stem_ut
            return d_stem_ut        
        

        if ftc == 'uu':
            from reversestem.dto.u import d_stem_uu
            return d_stem_uu        
        

        if ftc == 'uv':
            from reversestem.dto.u import d_stem_uv
            return d_stem_uv        
        

        if ftc == 'uw':
            from reversestem.dto.u import d_stem_uw
            return d_stem_uw        
        

        if ftc == 'uy':
            from reversestem.dto.u import d_stem_uy
            return d_stem_uy        
        

        if ftc == 'uz':
            from reversestem.dto.u import d_stem_uz
            return d_stem_uz        
        

    def unstem(self,
               input_text: str,
               flatten: bool = False) -> dict or list or None:
        input_text = input_text.lower().replace(' ', '_')
        return unstem_input(input_text=input_text,
                            d_trie_finder=self._get_trie,
                            flatten=flatten)
        
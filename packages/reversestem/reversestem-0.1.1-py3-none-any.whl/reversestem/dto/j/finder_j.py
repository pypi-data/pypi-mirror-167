
#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from reversestem.dmo import unstem_input


# AUTO GENERATED FINDER
class FinderJ(object):

    def _get_trie(self,
                  ftc: str) -> dict:

        
        if ftc == 'j_':
            from reversestem.dto.j import d_stem_j_
            return d_stem_j_        
        

        if ftc == 'ja':
            from reversestem.dto.j import d_stem_ja
            return d_stem_ja        
        

        if ftc == 'jb':
            from reversestem.dto.j import d_stem_jb
            return d_stem_jb        
        

        if ftc == 'jc':
            from reversestem.dto.j import d_stem_jc
            return d_stem_jc        
        

        if ftc == 'jd':
            from reversestem.dto.j import d_stem_jd
            return d_stem_jd        
        

        if ftc == 'je':
            from reversestem.dto.j import d_stem_je
            return d_stem_je        
        

        if ftc == 'jf':
            from reversestem.dto.j import d_stem_jf
            return d_stem_jf        
        

        if ftc == 'jg':
            from reversestem.dto.j import d_stem_jg
            return d_stem_jg        
        

        if ftc == 'jh':
            from reversestem.dto.j import d_stem_jh
            return d_stem_jh        
        

        if ftc == 'ji':
            from reversestem.dto.j import d_stem_ji
            return d_stem_ji        
        

        if ftc == 'jj':
            from reversestem.dto.j import d_stem_jj
            return d_stem_jj        
        

        if ftc == 'jk':
            from reversestem.dto.j import d_stem_jk
            return d_stem_jk        
        

        if ftc == 'jl':
            from reversestem.dto.j import d_stem_jl
            return d_stem_jl        
        

        if ftc == 'jm':
            from reversestem.dto.j import d_stem_jm
            return d_stem_jm        
        

        if ftc == 'jn':
            from reversestem.dto.j import d_stem_jn
            return d_stem_jn        
        

        if ftc == 'jo':
            from reversestem.dto.j import d_stem_jo
            return d_stem_jo        
        

        if ftc == 'jp':
            from reversestem.dto.j import d_stem_jp
            return d_stem_jp        
        

        if ftc == 'jq':
            from reversestem.dto.j import d_stem_jq
            return d_stem_jq        
        

        if ftc == 'jr':
            from reversestem.dto.j import d_stem_jr
            return d_stem_jr        
        

        if ftc == 'js':
            from reversestem.dto.j import d_stem_js
            return d_stem_js        
        

        if ftc == 'jt':
            from reversestem.dto.j import d_stem_jt
            return d_stem_jt        
        

        if ftc == 'ju':
            from reversestem.dto.j import d_stem_ju
            return d_stem_ju        
        

        if ftc == 'jv':
            from reversestem.dto.j import d_stem_jv
            return d_stem_jv        
        

        if ftc == 'jw':
            from reversestem.dto.j import d_stem_jw
            return d_stem_jw        
        

        if ftc == 'jy':
            from reversestem.dto.j import d_stem_jy
            return d_stem_jy        
        

        if ftc == 'jz':
            from reversestem.dto.j import d_stem_jz
            return d_stem_jz        
        

    def unstem(self,
               input_text: str,
               flatten: bool = False) -> dict or list or None:
        input_text = input_text.lower().replace(' ', '_')
        return unstem_input(input_text=input_text,
                            d_trie_finder=self._get_trie,
                            flatten=flatten)
        
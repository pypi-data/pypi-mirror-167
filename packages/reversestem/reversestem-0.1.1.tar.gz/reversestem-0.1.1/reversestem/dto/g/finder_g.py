
#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from reversestem.dmo import unstem_input


# AUTO GENERATED FINDER
class FinderG(object):

    def _get_trie(self,
                  ftc: str) -> dict:

        
        if ftc == 'g_':
            from reversestem.dto.g import d_stem_g_
            return d_stem_g_        
        

        if ftc == 'ga':
            from reversestem.dto.g import d_stem_ga
            return d_stem_ga        
        

        if ftc == 'gb':
            from reversestem.dto.g import d_stem_gb
            return d_stem_gb        
        

        if ftc == 'gc':
            from reversestem.dto.g import d_stem_gc
            return d_stem_gc        
        

        if ftc == 'gd':
            from reversestem.dto.g import d_stem_gd
            return d_stem_gd        
        

        if ftc == 'ge':
            from reversestem.dto.g import d_stem_ge
            return d_stem_ge        
        

        if ftc == 'gf':
            from reversestem.dto.g import d_stem_gf
            return d_stem_gf        
        

        if ftc == 'gg':
            from reversestem.dto.g import d_stem_gg
            return d_stem_gg        
        

        if ftc == 'gh':
            from reversestem.dto.g import d_stem_gh
            return d_stem_gh        
        

        if ftc == 'gi':
            from reversestem.dto.g import d_stem_gi
            return d_stem_gi        
        

        if ftc == 'gj':
            from reversestem.dto.g import d_stem_gj
            return d_stem_gj        
        

        if ftc == 'gk':
            from reversestem.dto.g import d_stem_gk
            return d_stem_gk        
        

        if ftc == 'gl':
            from reversestem.dto.g import d_stem_gl
            return d_stem_gl        
        

        if ftc == 'gm':
            from reversestem.dto.g import d_stem_gm
            return d_stem_gm        
        

        if ftc == 'gn':
            from reversestem.dto.g import d_stem_gn
            return d_stem_gn        
        

        if ftc == 'go':
            from reversestem.dto.g import d_stem_go
            return d_stem_go        
        

        if ftc == 'gp':
            from reversestem.dto.g import d_stem_gp
            return d_stem_gp        
        

        if ftc == 'gq':
            from reversestem.dto.g import d_stem_gq
            return d_stem_gq        
        

        if ftc == 'gr':
            from reversestem.dto.g import d_stem_gr
            return d_stem_gr        
        

        if ftc == 'gs':
            from reversestem.dto.g import d_stem_gs
            return d_stem_gs        
        

        if ftc == 'gt':
            from reversestem.dto.g import d_stem_gt
            return d_stem_gt        
        

        if ftc == 'gu':
            from reversestem.dto.g import d_stem_gu
            return d_stem_gu        
        

        if ftc == 'gv':
            from reversestem.dto.g import d_stem_gv
            return d_stem_gv        
        

        if ftc == 'gw':
            from reversestem.dto.g import d_stem_gw
            return d_stem_gw        
        

        if ftc == 'gy':
            from reversestem.dto.g import d_stem_gy
            return d_stem_gy        
        

        if ftc == 'gz':
            from reversestem.dto.g import d_stem_gz
            return d_stem_gz        
        

    def unstem(self,
               input_text: str,
               flatten: bool = False) -> dict or list or None:
        input_text = input_text.lower().replace(' ', '_')
        return unstem_input(input_text=input_text,
                            d_trie_finder=self._get_trie,
                            flatten=flatten)
        
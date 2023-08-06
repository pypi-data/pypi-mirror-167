
#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from reversestem.dmo import unstem_input


# AUTO GENERATED FINDER
class FinderW(object):

    def _get_trie(self,
                  ftc: str) -> dict:

        
        if ftc == 'w_':
            from reversestem.dto.w import d_stem_w_
            return d_stem_w_        
        

        if ftc == 'wa':
            from reversestem.dto.w import d_stem_wa
            return d_stem_wa        
        

        if ftc == 'wb':
            from reversestem.dto.w import d_stem_wb
            return d_stem_wb        
        

        if ftc == 'wc':
            from reversestem.dto.w import d_stem_wc
            return d_stem_wc        
        

        if ftc == 'wd':
            from reversestem.dto.w import d_stem_wd
            return d_stem_wd        
        

        if ftc == 'we':
            from reversestem.dto.w import d_stem_we
            return d_stem_we        
        

        if ftc == 'wf':
            from reversestem.dto.w import d_stem_wf
            return d_stem_wf        
        

        if ftc == 'wg':
            from reversestem.dto.w import d_stem_wg
            return d_stem_wg        
        

        if ftc == 'wh':
            from reversestem.dto.w import d_stem_wh
            return d_stem_wh        
        

        if ftc == 'wi':
            from reversestem.dto.w import d_stem_wi
            return d_stem_wi        
        

        if ftc == 'wj':
            from reversestem.dto.w import d_stem_wj
            return d_stem_wj        
        

        if ftc == 'wk':
            from reversestem.dto.w import d_stem_wk
            return d_stem_wk        
        

        if ftc == 'wl':
            from reversestem.dto.w import d_stem_wl
            return d_stem_wl        
        

        if ftc == 'wm':
            from reversestem.dto.w import d_stem_wm
            return d_stem_wm        
        

        if ftc == 'wn':
            from reversestem.dto.w import d_stem_wn
            return d_stem_wn        
        

        if ftc == 'wo':
            from reversestem.dto.w import d_stem_wo
            return d_stem_wo        
        

        if ftc == 'wp':
            from reversestem.dto.w import d_stem_wp
            return d_stem_wp        
        

        if ftc == 'wq':
            from reversestem.dto.w import d_stem_wq
            return d_stem_wq        
        

        if ftc == 'wr':
            from reversestem.dto.w import d_stem_wr
            return d_stem_wr        
        

        if ftc == 'ws':
            from reversestem.dto.w import d_stem_ws
            return d_stem_ws        
        

        if ftc == 'wt':
            from reversestem.dto.w import d_stem_wt
            return d_stem_wt        
        

        if ftc == 'wu':
            from reversestem.dto.w import d_stem_wu
            return d_stem_wu        
        

        if ftc == 'wv':
            from reversestem.dto.w import d_stem_wv
            return d_stem_wv        
        

        if ftc == 'ww':
            from reversestem.dto.w import d_stem_ww
            return d_stem_ww        
        

        if ftc == 'wy':
            from reversestem.dto.w import d_stem_wy
            return d_stem_wy        
        

        if ftc == 'wz':
            from reversestem.dto.w import d_stem_wz
            return d_stem_wz        
        

    def unstem(self,
               input_text: str,
               flatten: bool = False) -> dict or list or None:
        input_text = input_text.lower().replace(' ', '_')
        return unstem_input(input_text=input_text,
                            d_trie_finder=self._get_trie,
                            flatten=flatten)
        
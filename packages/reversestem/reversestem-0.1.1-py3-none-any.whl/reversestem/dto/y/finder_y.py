
#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from reversestem.dmo import unstem_input


# AUTO GENERATED FINDER
class FinderY(object):

    def _get_trie(self,
                  ftc: str) -> dict:

        
        if ftc == 'y_':
            from reversestem.dto.y import d_stem_y_
            return d_stem_y_        
        

        if ftc == 'ya':
            from reversestem.dto.y import d_stem_ya
            return d_stem_ya        
        

        if ftc == 'yb':
            from reversestem.dto.y import d_stem_yb
            return d_stem_yb        
        

        if ftc == 'yc':
            from reversestem.dto.y import d_stem_yc
            return d_stem_yc        
        

        if ftc == 'yd':
            from reversestem.dto.y import d_stem_yd
            return d_stem_yd        
        

        if ftc == 'ye':
            from reversestem.dto.y import d_stem_ye
            return d_stem_ye        
        

        if ftc == 'yf':
            from reversestem.dto.y import d_stem_yf
            return d_stem_yf        
        

        if ftc == 'yg':
            from reversestem.dto.y import d_stem_yg
            return d_stem_yg        
        

        if ftc == 'yh':
            from reversestem.dto.y import d_stem_yh
            return d_stem_yh        
        

        if ftc == 'yi':
            from reversestem.dto.y import d_stem_yi
            return d_stem_yi        
        

        if ftc == 'yj':
            from reversestem.dto.y import d_stem_yj
            return d_stem_yj        
        

        if ftc == 'yk':
            from reversestem.dto.y import d_stem_yk
            return d_stem_yk        
        

        if ftc == 'yl':
            from reversestem.dto.y import d_stem_yl
            return d_stem_yl        
        

        if ftc == 'ym':
            from reversestem.dto.y import d_stem_ym
            return d_stem_ym        
        

        if ftc == 'yn':
            from reversestem.dto.y import d_stem_yn
            return d_stem_yn        
        

        if ftc == 'yo':
            from reversestem.dto.y import d_stem_yo
            return d_stem_yo        
        

        if ftc == 'yp':
            from reversestem.dto.y import d_stem_yp
            return d_stem_yp        
        

        if ftc == 'yq':
            from reversestem.dto.y import d_stem_yq
            return d_stem_yq        
        

        if ftc == 'yr':
            from reversestem.dto.y import d_stem_yr
            return d_stem_yr        
        

        if ftc == 'ys':
            from reversestem.dto.y import d_stem_ys
            return d_stem_ys        
        

        if ftc == 'yt':
            from reversestem.dto.y import d_stem_yt
            return d_stem_yt        
        

        if ftc == 'yu':
            from reversestem.dto.y import d_stem_yu
            return d_stem_yu        
        

        if ftc == 'yv':
            from reversestem.dto.y import d_stem_yv
            return d_stem_yv        
        

        if ftc == 'yw':
            from reversestem.dto.y import d_stem_yw
            return d_stem_yw        
        

        if ftc == 'yy':
            from reversestem.dto.y import d_stem_yy
            return d_stem_yy        
        

        if ftc == 'yz':
            from reversestem.dto.y import d_stem_yz
            return d_stem_yz        
        

    def unstem(self,
               input_text: str,
               flatten: bool = False) -> dict or list or None:
        input_text = input_text.lower().replace(' ', '_')
        return unstem_input(input_text=input_text,
                            d_trie_finder=self._get_trie,
                            flatten=flatten)
        
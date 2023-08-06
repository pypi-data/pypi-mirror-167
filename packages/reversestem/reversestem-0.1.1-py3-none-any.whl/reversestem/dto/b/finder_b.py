
#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from reversestem.dmo import unstem_input


# AUTO GENERATED FINDER
class FinderB(object):

    def _get_trie(self,
                  ftc: str) -> dict:

        
        if ftc == 'b_':
            from reversestem.dto.b import d_stem_b_
            return d_stem_b_        
        

        if ftc == 'ba':
            from reversestem.dto.b import d_stem_ba
            return d_stem_ba        
        

        if ftc == 'bb':
            from reversestem.dto.b import d_stem_bb
            return d_stem_bb        
        

        if ftc == 'bc':
            from reversestem.dto.b import d_stem_bc
            return d_stem_bc        
        

        if ftc == 'bd':
            from reversestem.dto.b import d_stem_bd
            return d_stem_bd        
        

        if ftc == 'be':
            from reversestem.dto.b import d_stem_be
            return d_stem_be        
        

        if ftc == 'bf':
            from reversestem.dto.b import d_stem_bf
            return d_stem_bf        
        

        if ftc == 'bg':
            from reversestem.dto.b import d_stem_bg
            return d_stem_bg        
        

        if ftc == 'bh':
            from reversestem.dto.b import d_stem_bh
            return d_stem_bh        
        

        if ftc == 'bi':
            from reversestem.dto.b import d_stem_bi
            return d_stem_bi        
        

        if ftc == 'bj':
            from reversestem.dto.b import d_stem_bj
            return d_stem_bj        
        

        if ftc == 'bk':
            from reversestem.dto.b import d_stem_bk
            return d_stem_bk        
        

        if ftc == 'bl':
            from reversestem.dto.b import d_stem_bl
            return d_stem_bl        
        

        if ftc == 'bm':
            from reversestem.dto.b import d_stem_bm
            return d_stem_bm        
        

        if ftc == 'bn':
            from reversestem.dto.b import d_stem_bn
            return d_stem_bn        
        

        if ftc == 'bo':
            from reversestem.dto.b import d_stem_bo
            return d_stem_bo        
        

        if ftc == 'bp':
            from reversestem.dto.b import d_stem_bp
            return d_stem_bp        
        

        if ftc == 'bq':
            from reversestem.dto.b import d_stem_bq
            return d_stem_bq        
        

        if ftc == 'br':
            from reversestem.dto.b import d_stem_br
            return d_stem_br        
        

        if ftc == 'bs':
            from reversestem.dto.b import d_stem_bs
            return d_stem_bs        
        

        if ftc == 'bt':
            from reversestem.dto.b import d_stem_bt
            return d_stem_bt        
        

        if ftc == 'bu':
            from reversestem.dto.b import d_stem_bu
            return d_stem_bu        
        

        if ftc == 'bv':
            from reversestem.dto.b import d_stem_bv
            return d_stem_bv        
        

        if ftc == 'bw':
            from reversestem.dto.b import d_stem_bw
            return d_stem_bw        
        

        if ftc == 'by':
            from reversestem.dto.b import d_stem_by
            return d_stem_by        
        

        if ftc == 'bz':
            from reversestem.dto.b import d_stem_bz
            return d_stem_bz        
        

    def unstem(self,
               input_text: str,
               flatten: bool = False) -> dict or list or None:
        input_text = input_text.lower().replace(' ', '_')
        return unstem_input(input_text=input_text,
                            d_trie_finder=self._get_trie,
                            flatten=flatten)
        
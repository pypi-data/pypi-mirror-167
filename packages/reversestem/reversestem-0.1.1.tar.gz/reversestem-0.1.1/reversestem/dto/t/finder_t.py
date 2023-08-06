
#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from reversestem.dmo import unstem_input


# AUTO GENERATED FINDER
class FinderT(object):

    def _get_trie(self,
                  ftc: str) -> dict:

        
        if ftc == 't_':
            from reversestem.dto.t import d_stem_t_
            return d_stem_t_        
        

        if ftc == 'ta':
            from reversestem.dto.t import d_stem_ta
            return d_stem_ta        
        

        if ftc == 'tb':
            from reversestem.dto.t import d_stem_tb
            return d_stem_tb        
        

        if ftc == 'tc':
            from reversestem.dto.t import d_stem_tc
            return d_stem_tc        
        

        if ftc == 'td':
            from reversestem.dto.t import d_stem_td
            return d_stem_td        
        

        if ftc == 'te':
            from reversestem.dto.t import d_stem_te
            return d_stem_te        
        

        if ftc == 'tf':
            from reversestem.dto.t import d_stem_tf
            return d_stem_tf        
        

        if ftc == 'tg':
            from reversestem.dto.t import d_stem_tg
            return d_stem_tg        
        

        if ftc == 'th':
            from reversestem.dto.t import d_stem_th
            return d_stem_th        
        

        if ftc == 'ti':
            from reversestem.dto.t import d_stem_ti
            return d_stem_ti        
        

        if ftc == 'tj':
            from reversestem.dto.t import d_stem_tj
            return d_stem_tj        
        

        if ftc == 'tk':
            from reversestem.dto.t import d_stem_tk
            return d_stem_tk        
        

        if ftc == 'tl':
            from reversestem.dto.t import d_stem_tl
            return d_stem_tl        
        

        if ftc == 'tm':
            from reversestem.dto.t import d_stem_tm
            return d_stem_tm        
        

        if ftc == 'tn':
            from reversestem.dto.t import d_stem_tn
            return d_stem_tn        
        

        if ftc == 'to':
            from reversestem.dto.t import d_stem_to
            return d_stem_to        
        

        if ftc == 'tp':
            from reversestem.dto.t import d_stem_tp
            return d_stem_tp        
        

        if ftc == 'tq':
            from reversestem.dto.t import d_stem_tq
            return d_stem_tq        
        

        if ftc == 'tr':
            from reversestem.dto.t import d_stem_tr
            return d_stem_tr        
        

        if ftc == 'ts':
            from reversestem.dto.t import d_stem_ts
            return d_stem_ts        
        

        if ftc == 'tt':
            from reversestem.dto.t import d_stem_tt
            return d_stem_tt        
        

        if ftc == 'tu':
            from reversestem.dto.t import d_stem_tu
            return d_stem_tu        
        

        if ftc == 'tv':
            from reversestem.dto.t import d_stem_tv
            return d_stem_tv        
        

        if ftc == 'tw':
            from reversestem.dto.t import d_stem_tw
            return d_stem_tw        
        

        if ftc == 'ty':
            from reversestem.dto.t import d_stem_ty
            return d_stem_ty        
        

        if ftc == 'tz':
            from reversestem.dto.t import d_stem_tz
            return d_stem_tz        
        

    def unstem(self,
               input_text: str,
               flatten: bool = False) -> dict or list or None:
        input_text = input_text.lower().replace(' ', '_')
        return unstem_input(input_text=input_text,
                            d_trie_finder=self._get_trie,
                            flatten=flatten)
        

#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from reversestem.dmo import unstem_input


# AUTO GENERATED FINDER
class FinderK(object):

    def _get_trie(self,
                  ftc: str) -> dict:

        
        if ftc == 'k_':
            from reversestem.dto.k import d_stem_k_
            return d_stem_k_        
        

        if ftc == 'ka':
            from reversestem.dto.k import d_stem_ka
            return d_stem_ka        
        

        if ftc == 'kb':
            from reversestem.dto.k import d_stem_kb
            return d_stem_kb        
        

        if ftc == 'kc':
            from reversestem.dto.k import d_stem_kc
            return d_stem_kc        
        

        if ftc == 'kd':
            from reversestem.dto.k import d_stem_kd
            return d_stem_kd        
        

        if ftc == 'ke':
            from reversestem.dto.k import d_stem_ke
            return d_stem_ke        
        

        if ftc == 'kf':
            from reversestem.dto.k import d_stem_kf
            return d_stem_kf        
        

        if ftc == 'kg':
            from reversestem.dto.k import d_stem_kg
            return d_stem_kg        
        

        if ftc == 'kh':
            from reversestem.dto.k import d_stem_kh
            return d_stem_kh        
        

        if ftc == 'ki':
            from reversestem.dto.k import d_stem_ki
            return d_stem_ki        
        

        if ftc == 'kj':
            from reversestem.dto.k import d_stem_kj
            return d_stem_kj        
        

        if ftc == 'kk':
            from reversestem.dto.k import d_stem_kk
            return d_stem_kk        
        

        if ftc == 'kl':
            from reversestem.dto.k import d_stem_kl
            return d_stem_kl        
        

        if ftc == 'km':
            from reversestem.dto.k import d_stem_km
            return d_stem_km        
        

        if ftc == 'kn':
            from reversestem.dto.k import d_stem_kn
            return d_stem_kn        
        

        if ftc == 'ko':
            from reversestem.dto.k import d_stem_ko
            return d_stem_ko        
        

        if ftc == 'kp':
            from reversestem.dto.k import d_stem_kp
            return d_stem_kp        
        

        if ftc == 'kq':
            from reversestem.dto.k import d_stem_kq
            return d_stem_kq        
        

        if ftc == 'kr':
            from reversestem.dto.k import d_stem_kr
            return d_stem_kr        
        

        if ftc == 'ks':
            from reversestem.dto.k import d_stem_ks
            return d_stem_ks        
        

        if ftc == 'kt':
            from reversestem.dto.k import d_stem_kt
            return d_stem_kt        
        

        if ftc == 'ku':
            from reversestem.dto.k import d_stem_ku
            return d_stem_ku        
        

        if ftc == 'kv':
            from reversestem.dto.k import d_stem_kv
            return d_stem_kv        
        

        if ftc == 'kw':
            from reversestem.dto.k import d_stem_kw
            return d_stem_kw        
        

        if ftc == 'ky':
            from reversestem.dto.k import d_stem_ky
            return d_stem_ky        
        

        if ftc == 'kz':
            from reversestem.dto.k import d_stem_kz
            return d_stem_kz        
        

    def unstem(self,
               input_text: str,
               flatten: bool = False) -> dict or list or None:
        input_text = input_text.lower().replace(' ', '_')
        return unstem_input(input_text=input_text,
                            d_trie_finder=self._get_trie,
                            flatten=flatten)
        
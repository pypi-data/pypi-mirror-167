
#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from reversestem.dmo import unstem_input


# AUTO GENERATED FINDER
class FinderE(object):

    def _get_trie(self,
                  ftc: str) -> dict:

        
        if ftc == 'e_':
            from reversestem.dto.e import d_stem_e_
            return d_stem_e_        
        

        if ftc == 'ea':
            from reversestem.dto.e import d_stem_ea
            return d_stem_ea        
        

        if ftc == 'eb':
            from reversestem.dto.e import d_stem_eb
            return d_stem_eb        
        

        if ftc == 'ec':
            from reversestem.dto.e import d_stem_ec
            return d_stem_ec        
        

        if ftc == 'ed':
            from reversestem.dto.e import d_stem_ed
            return d_stem_ed        
        

        if ftc == 'ee':
            from reversestem.dto.e import d_stem_ee
            return d_stem_ee        
        

        if ftc == 'ef':
            from reversestem.dto.e import d_stem_ef
            return d_stem_ef        
        

        if ftc == 'eg':
            from reversestem.dto.e import d_stem_eg
            return d_stem_eg        
        

        if ftc == 'eh':
            from reversestem.dto.e import d_stem_eh
            return d_stem_eh        
        

        if ftc == 'ei':
            from reversestem.dto.e import d_stem_ei
            return d_stem_ei        
        

        if ftc == 'ej':
            from reversestem.dto.e import d_stem_ej
            return d_stem_ej        
        

        if ftc == 'ek':
            from reversestem.dto.e import d_stem_ek
            return d_stem_ek        
        

        if ftc == 'el':
            from reversestem.dto.e import d_stem_el
            return d_stem_el        
        

        if ftc == 'em':
            from reversestem.dto.e import d_stem_em
            return d_stem_em        
        

        if ftc == 'en':
            from reversestem.dto.e import d_stem_en
            return d_stem_en        
        

        if ftc == 'eo':
            from reversestem.dto.e import d_stem_eo
            return d_stem_eo        
        

        if ftc == 'ep':
            from reversestem.dto.e import d_stem_ep
            return d_stem_ep        
        

        if ftc == 'eq':
            from reversestem.dto.e import d_stem_eq
            return d_stem_eq        
        

        if ftc == 'er':
            from reversestem.dto.e import d_stem_er
            return d_stem_er        
        

        if ftc == 'es':
            from reversestem.dto.e import d_stem_es
            return d_stem_es        
        

        if ftc == 'et':
            from reversestem.dto.e import d_stem_et
            return d_stem_et        
        

        if ftc == 'eu':
            from reversestem.dto.e import d_stem_eu
            return d_stem_eu        
        

        if ftc == 'ev':
            from reversestem.dto.e import d_stem_ev
            return d_stem_ev        
        

        if ftc == 'ew':
            from reversestem.dto.e import d_stem_ew
            return d_stem_ew        
        

        if ftc == 'ey':
            from reversestem.dto.e import d_stem_ey
            return d_stem_ey        
        

        if ftc == 'ez':
            from reversestem.dto.e import d_stem_ez
            return d_stem_ez        
        

    def unstem(self,
               input_text: str,
               flatten: bool = False) -> dict or list or None:
        input_text = input_text.lower().replace(' ', '_')
        return unstem_input(input_text=input_text,
                            d_trie_finder=self._get_trie,
                            flatten=flatten)
        
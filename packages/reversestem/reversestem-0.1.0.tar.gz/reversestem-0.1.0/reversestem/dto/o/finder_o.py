
#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from reversestem.dmo import unstem_input


# AUTO GENERATED FINDER
class FinderO(object):

    def _get_trie(self,
                  ftc: str) -> dict:

        
        if ftc == 'o_':
            from reversestem.dto.o import d_stem_o_
            return d_stem_o_        
        

        if ftc == 'oa':
            from reversestem.dto.o import d_stem_oa
            return d_stem_oa        
        

        if ftc == 'ob':
            from reversestem.dto.o import d_stem_ob
            return d_stem_ob        
        

        if ftc == 'oc':
            from reversestem.dto.o import d_stem_oc
            return d_stem_oc        
        

        if ftc == 'od':
            from reversestem.dto.o import d_stem_od
            return d_stem_od        
        

        if ftc == 'oe':
            from reversestem.dto.o import d_stem_oe
            return d_stem_oe        
        

        if ftc == 'of':
            from reversestem.dto.o import d_stem_of
            return d_stem_of        
        

        if ftc == 'og':
            from reversestem.dto.o import d_stem_og
            return d_stem_og        
        

        if ftc == 'oh':
            from reversestem.dto.o import d_stem_oh
            return d_stem_oh        
        

        if ftc == 'oi':
            from reversestem.dto.o import d_stem_oi
            return d_stem_oi        
        

        if ftc == 'oj':
            from reversestem.dto.o import d_stem_oj
            return d_stem_oj        
        

        if ftc == 'ok':
            from reversestem.dto.o import d_stem_ok
            return d_stem_ok        
        

        if ftc == 'ol':
            from reversestem.dto.o import d_stem_ol
            return d_stem_ol        
        

        if ftc == 'om':
            from reversestem.dto.o import d_stem_om
            return d_stem_om        
        

        if ftc == 'on':
            from reversestem.dto.o import d_stem_on
            return d_stem_on        
        

        if ftc == 'oo':
            from reversestem.dto.o import d_stem_oo
            return d_stem_oo        
        

        if ftc == 'op':
            from reversestem.dto.o import d_stem_op
            return d_stem_op        
        

        if ftc == 'oq':
            from reversestem.dto.o import d_stem_oq
            return d_stem_oq        
        

        if ftc == 'or':
            from reversestem.dto.o import d_stem_or
            return d_stem_or        
        

        if ftc == 'os':
            from reversestem.dto.o import d_stem_os
            return d_stem_os        
        

        if ftc == 'ot':
            from reversestem.dto.o import d_stem_ot
            return d_stem_ot        
        

        if ftc == 'ou':
            from reversestem.dto.o import d_stem_ou
            return d_stem_ou        
        

        if ftc == 'ov':
            from reversestem.dto.o import d_stem_ov
            return d_stem_ov        
        

        if ftc == 'ow':
            from reversestem.dto.o import d_stem_ow
            return d_stem_ow        
        

        if ftc == 'oy':
            from reversestem.dto.o import d_stem_oy
            return d_stem_oy        
        

        if ftc == 'oz':
            from reversestem.dto.o import d_stem_oz
            return d_stem_oz        
        

    def unstem(self,
               input_text: str,
               flatten: bool = False) -> dict or list or None:
        input_text = input_text.lower().replace(' ', '_')
        return unstem_input(input_text=input_text,
                            d_trie_finder=self._get_trie,
                            flatten=flatten)
        
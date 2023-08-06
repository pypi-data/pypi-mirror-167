
#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from reversestem.dmo import unstem_input


# AUTO GENERATED FINDER
class FinderI(object):

    def _get_trie(self,
                  ftc: str) -> dict:

        
        if ftc == 'i_':
            from reversestem.dto.i import d_stem_i_
            return d_stem_i_        
        

        if ftc == 'ia':
            from reversestem.dto.i import d_stem_ia
            return d_stem_ia        
        

        if ftc == 'ib':
            from reversestem.dto.i import d_stem_ib
            return d_stem_ib        
        

        if ftc == 'ic':
            from reversestem.dto.i import d_stem_ic
            return d_stem_ic        
        

        if ftc == 'id':
            from reversestem.dto.i import d_stem_id
            return d_stem_id        
        

        if ftc == 'ie':
            from reversestem.dto.i import d_stem_ie
            return d_stem_ie        
        

        if ftc == 'if':
            from reversestem.dto.i import d_stem_if
            return d_stem_if        
        

        if ftc == 'ig':
            from reversestem.dto.i import d_stem_ig
            return d_stem_ig        
        

        if ftc == 'ih':
            from reversestem.dto.i import d_stem_ih
            return d_stem_ih        
        

        if ftc == 'ii':
            from reversestem.dto.i import d_stem_ii
            return d_stem_ii        
        

        if ftc == 'ij':
            from reversestem.dto.i import d_stem_ij
            return d_stem_ij        
        

        if ftc == 'ik':
            from reversestem.dto.i import d_stem_ik
            return d_stem_ik        
        

        if ftc == 'il':
            from reversestem.dto.i import d_stem_il
            return d_stem_il        
        

        if ftc == 'im':
            from reversestem.dto.i import d_stem_im
            return d_stem_im        
        

        if ftc == 'in':
            from reversestem.dto.i import d_stem_in
            return d_stem_in        
        

        if ftc == 'io':
            from reversestem.dto.i import d_stem_io
            return d_stem_io        
        

        if ftc == 'ip':
            from reversestem.dto.i import d_stem_ip
            return d_stem_ip        
        

        if ftc == 'iq':
            from reversestem.dto.i import d_stem_iq
            return d_stem_iq        
        

        if ftc == 'ir':
            from reversestem.dto.i import d_stem_ir
            return d_stem_ir        
        

        if ftc == 'is':
            from reversestem.dto.i import d_stem_is
            return d_stem_is        
        

        if ftc == 'it':
            from reversestem.dto.i import d_stem_it
            return d_stem_it        
        

        if ftc == 'iu':
            from reversestem.dto.i import d_stem_iu
            return d_stem_iu        
        

        if ftc == 'iv':
            from reversestem.dto.i import d_stem_iv
            return d_stem_iv        
        

        if ftc == 'iw':
            from reversestem.dto.i import d_stem_iw
            return d_stem_iw        
        

        if ftc == 'iy':
            from reversestem.dto.i import d_stem_iy
            return d_stem_iy        
        

        if ftc == 'iz':
            from reversestem.dto.i import d_stem_iz
            return d_stem_iz        
        

    def unstem(self,
               input_text: str,
               flatten: bool = False) -> dict or list or None:
        input_text = input_text.lower().replace(' ', '_')
        return unstem_input(input_text=input_text,
                            d_trie_finder=self._get_trie,
                            flatten=flatten)
        
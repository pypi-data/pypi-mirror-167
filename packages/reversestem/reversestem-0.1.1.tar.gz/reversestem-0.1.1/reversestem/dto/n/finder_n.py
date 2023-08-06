
#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from reversestem.dmo import unstem_input


# AUTO GENERATED FINDER
class FinderN(object):

    def _get_trie(self,
                  ftc: str) -> dict:

        
        if ftc == 'n_':
            from reversestem.dto.n import d_stem_n_
            return d_stem_n_        
        

        if ftc == 'na':
            from reversestem.dto.n import d_stem_na
            return d_stem_na        
        

        if ftc == 'nb':
            from reversestem.dto.n import d_stem_nb
            return d_stem_nb        
        

        if ftc == 'nc':
            from reversestem.dto.n import d_stem_nc
            return d_stem_nc        
        

        if ftc == 'nd':
            from reversestem.dto.n import d_stem_nd
            return d_stem_nd        
        

        if ftc == 'ne':
            from reversestem.dto.n import d_stem_ne
            return d_stem_ne        
        

        if ftc == 'nf':
            from reversestem.dto.n import d_stem_nf
            return d_stem_nf        
        

        if ftc == 'ng':
            from reversestem.dto.n import d_stem_ng
            return d_stem_ng        
        

        if ftc == 'nh':
            from reversestem.dto.n import d_stem_nh
            return d_stem_nh        
        

        if ftc == 'ni':
            from reversestem.dto.n import d_stem_ni
            return d_stem_ni        
        

        if ftc == 'nj':
            from reversestem.dto.n import d_stem_nj
            return d_stem_nj        
        

        if ftc == 'nk':
            from reversestem.dto.n import d_stem_nk
            return d_stem_nk        
        

        if ftc == 'nl':
            from reversestem.dto.n import d_stem_nl
            return d_stem_nl        
        

        if ftc == 'nm':
            from reversestem.dto.n import d_stem_nm
            return d_stem_nm        
        

        if ftc == 'nn':
            from reversestem.dto.n import d_stem_nn
            return d_stem_nn        
        

        if ftc == 'no':
            from reversestem.dto.n import d_stem_no
            return d_stem_no        
        

        if ftc == 'np':
            from reversestem.dto.n import d_stem_np
            return d_stem_np        
        

        if ftc == 'nq':
            from reversestem.dto.n import d_stem_nq
            return d_stem_nq        
        

        if ftc == 'nr':
            from reversestem.dto.n import d_stem_nr
            return d_stem_nr        
        

        if ftc == 'ns':
            from reversestem.dto.n import d_stem_ns
            return d_stem_ns        
        

        if ftc == 'nt':
            from reversestem.dto.n import d_stem_nt
            return d_stem_nt        
        

        if ftc == 'nu':
            from reversestem.dto.n import d_stem_nu
            return d_stem_nu        
        

        if ftc == 'nv':
            from reversestem.dto.n import d_stem_nv
            return d_stem_nv        
        

        if ftc == 'nw':
            from reversestem.dto.n import d_stem_nw
            return d_stem_nw        
        

        if ftc == 'ny':
            from reversestem.dto.n import d_stem_ny
            return d_stem_ny        
        

        if ftc == 'nz':
            from reversestem.dto.n import d_stem_nz
            return d_stem_nz        
        

    def unstem(self,
               input_text: str,
               flatten: bool = False) -> dict or list or None:
        input_text = input_text.lower().replace(' ', '_')
        return unstem_input(input_text=input_text,
                            d_trie_finder=self._get_trie,
                            flatten=flatten)
        
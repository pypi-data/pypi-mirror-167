
#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from reversestem.dmo import unstem_input


# AUTO GENERATED FINDER
class FinderP(object):

    def _get_trie(self,
                  ftc: str) -> dict:

        
        if ftc == 'p_':
            from reversestem.dto.p import d_stem_p_
            return d_stem_p_        
        

        if ftc == 'pa':
            from reversestem.dto.p import d_stem_pa
            return d_stem_pa        
        

        if ftc == 'pb':
            from reversestem.dto.p import d_stem_pb
            return d_stem_pb        
        

        if ftc == 'pc':
            from reversestem.dto.p import d_stem_pc
            return d_stem_pc        
        

        if ftc == 'pd':
            from reversestem.dto.p import d_stem_pd
            return d_stem_pd        
        

        if ftc == 'pe':
            from reversestem.dto.p import d_stem_pe
            return d_stem_pe        
        

        if ftc == 'pf':
            from reversestem.dto.p import d_stem_pf
            return d_stem_pf        
        

        if ftc == 'pg':
            from reversestem.dto.p import d_stem_pg
            return d_stem_pg        
        

        if ftc == 'ph':
            from reversestem.dto.p import d_stem_ph
            return d_stem_ph        
        

        if ftc == 'pi':
            from reversestem.dto.p import d_stem_pi
            return d_stem_pi        
        

        if ftc == 'pj':
            from reversestem.dto.p import d_stem_pj
            return d_stem_pj        
        

        if ftc == 'pk':
            from reversestem.dto.p import d_stem_pk
            return d_stem_pk        
        

        if ftc == 'pl':
            from reversestem.dto.p import d_stem_pl
            return d_stem_pl        
        

        if ftc == 'pm':
            from reversestem.dto.p import d_stem_pm
            return d_stem_pm        
        

        if ftc == 'pn':
            from reversestem.dto.p import d_stem_pn
            return d_stem_pn        
        

        if ftc == 'po':
            from reversestem.dto.p import d_stem_po
            return d_stem_po        
        

        if ftc == 'pp':
            from reversestem.dto.p import d_stem_pp
            return d_stem_pp        
        

        if ftc == 'pq':
            from reversestem.dto.p import d_stem_pq
            return d_stem_pq        
        

        if ftc == 'pr':
            from reversestem.dto.p import d_stem_pr
            return d_stem_pr        
        

        if ftc == 'ps':
            from reversestem.dto.p import d_stem_ps
            return d_stem_ps        
        

        if ftc == 'pt':
            from reversestem.dto.p import d_stem_pt
            return d_stem_pt        
        

        if ftc == 'pu':
            from reversestem.dto.p import d_stem_pu
            return d_stem_pu        
        

        if ftc == 'pv':
            from reversestem.dto.p import d_stem_pv
            return d_stem_pv        
        

        if ftc == 'pw':
            from reversestem.dto.p import d_stem_pw
            return d_stem_pw        
        

        if ftc == 'py':
            from reversestem.dto.p import d_stem_py
            return d_stem_py        
        

        if ftc == 'pz':
            from reversestem.dto.p import d_stem_pz
            return d_stem_pz        
        

    def unstem(self,
               input_text: str,
               flatten: bool = False) -> dict or list or None:
        input_text = input_text.lower().replace(' ', '_')
        return unstem_input(input_text=input_text,
                            d_trie_finder=self._get_trie,
                            flatten=flatten)
        
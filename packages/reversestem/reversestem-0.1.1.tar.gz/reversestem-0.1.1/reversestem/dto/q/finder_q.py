
#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from reversestem.dmo import unstem_input


# AUTO GENERATED FINDER
class FinderQ(object):

    def _get_trie(self,
                  ftc: str) -> dict:

        
        if ftc == 'q_':
            from reversestem.dto.q import d_stem_q_
            return d_stem_q_        
        

        if ftc == 'qa':
            from reversestem.dto.q import d_stem_qa
            return d_stem_qa        
        

        if ftc == 'qb':
            from reversestem.dto.q import d_stem_qb
            return d_stem_qb        
        

        if ftc == 'qc':
            from reversestem.dto.q import d_stem_qc
            return d_stem_qc        
        

        if ftc == 'qd':
            from reversestem.dto.q import d_stem_qd
            return d_stem_qd        
        

        if ftc == 'qe':
            from reversestem.dto.q import d_stem_qe
            return d_stem_qe        
        

        if ftc == 'qf':
            from reversestem.dto.q import d_stem_qf
            return d_stem_qf        
        

        if ftc == 'qg':
            from reversestem.dto.q import d_stem_qg
            return d_stem_qg        
        

        if ftc == 'qh':
            from reversestem.dto.q import d_stem_qh
            return d_stem_qh        
        

        if ftc == 'qi':
            from reversestem.dto.q import d_stem_qi
            return d_stem_qi        
        

        if ftc == 'qj':
            from reversestem.dto.q import d_stem_qj
            return d_stem_qj        
        

        if ftc == 'qk':
            from reversestem.dto.q import d_stem_qk
            return d_stem_qk        
        

        if ftc == 'ql':
            from reversestem.dto.q import d_stem_ql
            return d_stem_ql        
        

        if ftc == 'qm':
            from reversestem.dto.q import d_stem_qm
            return d_stem_qm        
        

        if ftc == 'qn':
            from reversestem.dto.q import d_stem_qn
            return d_stem_qn        
        

        if ftc == 'qo':
            from reversestem.dto.q import d_stem_qo
            return d_stem_qo        
        

        if ftc == 'qp':
            from reversestem.dto.q import d_stem_qp
            return d_stem_qp        
        

        if ftc == 'qq':
            from reversestem.dto.q import d_stem_qq
            return d_stem_qq        
        

        if ftc == 'qr':
            from reversestem.dto.q import d_stem_qr
            return d_stem_qr        
        

        if ftc == 'qs':
            from reversestem.dto.q import d_stem_qs
            return d_stem_qs        
        

        if ftc == 'qt':
            from reversestem.dto.q import d_stem_qt
            return d_stem_qt        
        

        if ftc == 'qu':
            from reversestem.dto.q import d_stem_qu
            return d_stem_qu        
        

        if ftc == 'qv':
            from reversestem.dto.q import d_stem_qv
            return d_stem_qv        
        

        if ftc == 'qw':
            from reversestem.dto.q import d_stem_qw
            return d_stem_qw        
        

        if ftc == 'qy':
            from reversestem.dto.q import d_stem_qy
            return d_stem_qy        
        

        if ftc == 'qz':
            from reversestem.dto.q import d_stem_qz
            return d_stem_qz        
        

    def unstem(self,
               input_text: str,
               flatten: bool = False) -> dict or list or None:
        input_text = input_text.lower().replace(' ', '_')
        return unstem_input(input_text=input_text,
                            d_trie_finder=self._get_trie,
                            flatten=flatten)
        
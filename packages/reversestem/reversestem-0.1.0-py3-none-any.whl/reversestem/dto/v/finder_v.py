
#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from reversestem.dmo import unstem_input


# AUTO GENERATED FINDER
class FinderV(object):

    def _get_trie(self,
                  ftc: str) -> dict:

        
        if ftc == 'v_':
            from reversestem.dto.v import d_stem_v_
            return d_stem_v_        
        

        if ftc == 'va':
            from reversestem.dto.v import d_stem_va
            return d_stem_va        
        

        if ftc == 'vb':
            from reversestem.dto.v import d_stem_vb
            return d_stem_vb        
        

        if ftc == 'vc':
            from reversestem.dto.v import d_stem_vc
            return d_stem_vc        
        

        if ftc == 'vd':
            from reversestem.dto.v import d_stem_vd
            return d_stem_vd        
        

        if ftc == 've':
            from reversestem.dto.v import d_stem_ve
            return d_stem_ve        
        

        if ftc == 'vf':
            from reversestem.dto.v import d_stem_vf
            return d_stem_vf        
        

        if ftc == 'vg':
            from reversestem.dto.v import d_stem_vg
            return d_stem_vg        
        

        if ftc == 'vh':
            from reversestem.dto.v import d_stem_vh
            return d_stem_vh        
        

        if ftc == 'vi':
            from reversestem.dto.v import d_stem_vi
            return d_stem_vi        
        

        if ftc == 'vj':
            from reversestem.dto.v import d_stem_vj
            return d_stem_vj        
        

        if ftc == 'vk':
            from reversestem.dto.v import d_stem_vk
            return d_stem_vk        
        

        if ftc == 'vl':
            from reversestem.dto.v import d_stem_vl
            return d_stem_vl        
        

        if ftc == 'vm':
            from reversestem.dto.v import d_stem_vm
            return d_stem_vm        
        

        if ftc == 'vn':
            from reversestem.dto.v import d_stem_vn
            return d_stem_vn        
        

        if ftc == 'vo':
            from reversestem.dto.v import d_stem_vo
            return d_stem_vo        
        

        if ftc == 'vp':
            from reversestem.dto.v import d_stem_vp
            return d_stem_vp        
        

        if ftc == 'vq':
            from reversestem.dto.v import d_stem_vq
            return d_stem_vq        
        

        if ftc == 'vr':
            from reversestem.dto.v import d_stem_vr
            return d_stem_vr        
        

        if ftc == 'vs':
            from reversestem.dto.v import d_stem_vs
            return d_stem_vs        
        

        if ftc == 'vt':
            from reversestem.dto.v import d_stem_vt
            return d_stem_vt        
        

        if ftc == 'vu':
            from reversestem.dto.v import d_stem_vu
            return d_stem_vu        
        

        if ftc == 'vv':
            from reversestem.dto.v import d_stem_vv
            return d_stem_vv        
        

        if ftc == 'vw':
            from reversestem.dto.v import d_stem_vw
            return d_stem_vw        
        

        if ftc == 'vy':
            from reversestem.dto.v import d_stem_vy
            return d_stem_vy        
        

        if ftc == 'vz':
            from reversestem.dto.v import d_stem_vz
            return d_stem_vz        
        

    def unstem(self,
               input_text: str,
               flatten: bool = False) -> dict or list or None:
        input_text = input_text.lower().replace(' ', '_')
        return unstem_input(input_text=input_text,
                            d_trie_finder=self._get_trie,
                            flatten=flatten)
        
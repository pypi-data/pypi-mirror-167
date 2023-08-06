
#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from typing import Callable


class StemFinder(object):

    __cache_finder = {}

    def _get_finder(self,
                    first_char: str) -> Callable:

        if first_char in self.__cache_finder:
            return self.__cache_finder[first_char]

        if first_char == 'a':
            from reversestem.dto.a import FinderA
            self.__cache_finder[first_char] = FinderA().unstem

        if first_char == 'b':
            from reversestem.dto.b import FinderB
            self.__cache_finder[first_char] = FinderB().unstem

        if first_char == 'c':
            from reversestem.dto.c import FinderC
            self.__cache_finder[first_char] = FinderC().unstem

        if first_char == 'd':
            from reversestem.dto.d import FinderD
            self.__cache_finder[first_char] = FinderD().unstem

        if first_char == 'e':
            from reversestem.dto.e import FinderE
            self.__cache_finder[first_char] = FinderE().unstem

        if first_char == 'f':
            from reversestem.dto.f import FinderF
            self.__cache_finder[first_char] = FinderF().unstem

        if first_char == 'g':
            from reversestem.dto.g import FinderG
            self.__cache_finder[first_char] = FinderG().unstem

        if first_char == 'h':
            from reversestem.dto.h import FinderH
            self.__cache_finder[first_char] = FinderH().unstem

        if first_char == 'i':
            from reversestem.dto.i import FinderI
            self.__cache_finder[first_char] = FinderI().unstem

        if first_char == 'j':
            from reversestem.dto.j import FinderJ
            self.__cache_finder[first_char] = FinderJ().unstem

        if first_char == 'k':
            from reversestem.dto.k import FinderK
            self.__cache_finder[first_char] = FinderK().unstem

        if first_char == 'l':
            from reversestem.dto.l import FinderL
            self.__cache_finder[first_char] = FinderL().unstem

        if first_char == 'm':
            from reversestem.dto.m import FinderM
            self.__cache_finder[first_char] = FinderM().unstem

        if first_char == 'n':
            from reversestem.dto.n import FinderN
            self.__cache_finder[first_char] = FinderN().unstem

        if first_char == 'o':
            from reversestem.dto.o import FinderO
            self.__cache_finder[first_char] = FinderO().unstem

        if first_char == 'p':
            from reversestem.dto.p import FinderP
            self.__cache_finder[first_char] = FinderP().unstem

        if first_char == 'q':
            from reversestem.dto.q import FinderQ
            self.__cache_finder[first_char] = FinderQ().unstem

        if first_char == 'r':
            from reversestem.dto.r import FinderR
            self.__cache_finder[first_char] = FinderR().unstem

        if first_char == 's':
            from reversestem.dto.s import FinderS
            self.__cache_finder[first_char] = FinderS().unstem

        if first_char == 't':
            from reversestem.dto.t import FinderT
            self.__cache_finder[first_char] = FinderT().unstem

        if first_char == 'u':
            from reversestem.dto.u import FinderU
            self.__cache_finder[first_char] = FinderU().unstem

        if first_char == 'v':
            from reversestem.dto.v import FinderV
            self.__cache_finder[first_char] = FinderV().unstem

        if first_char == 'w':
            from reversestem.dto.w import FinderW
            self.__cache_finder[first_char] = FinderW().unstem

        # if first_char == 'x':
        #     from reversestem.dto.x import FinderX
        #     self.__cache_finder[first_char] = FinderX().unstem

        if first_char == 'y':
            from reversestem.dto.y import FinderY
            self.__cache_finder[first_char] = FinderY().unstem

        if first_char == 'z':
            from reversestem.dto.z import FinderZ
            self.__cache_finder[first_char] = FinderZ().unstem

        if first_char in self.__cache_finder:
            return self.__cache_finder[first_char]

    def unstem(self,
               input_text: str,
               flatten: bool = False) -> dict or list or None:
        input_text = input_text.lower()
        finder_cb = self._get_finder(input_text[0])
        if finder_cb:
            return finder_cb(input_text=input_text,
                             flatten=flatten)

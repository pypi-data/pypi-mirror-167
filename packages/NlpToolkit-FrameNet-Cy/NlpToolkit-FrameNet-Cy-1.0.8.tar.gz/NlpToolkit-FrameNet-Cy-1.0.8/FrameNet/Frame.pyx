cdef class Frame:

    def __init__(self, name: str):
        self.__lexical_units = []
        self.__frame_elements = []
        self.__name = name

    cpdef addLexicalUnit(self, str lexicalUnit):
        self.__lexical_units.append(lexicalUnit)

    cpdef addFrameElement(self, str frameElement):
        self.__frame_elements.append(frameElement)

    cpdef bint lexicalUnitExists(self, str synSetId):
        return synSetId in self.__lexical_units

    cpdef str getLexicalUnit(self, int index):
        return self.__lexical_units[index]

    cpdef str getFrameElement(self, int index):
        return self.__frame_elements[index]

    cpdef int lexicalUnitSize(self):
        return len(self.__lexical_units)

    cpdef int frameElementSize(self):
        return len(self.__frame_elements)

    cpdef str getName(self):
        return self.__name

    def __repr__(self):
        return f"{self.__name} {self.__lexical_units} {self.__frame_elements}"

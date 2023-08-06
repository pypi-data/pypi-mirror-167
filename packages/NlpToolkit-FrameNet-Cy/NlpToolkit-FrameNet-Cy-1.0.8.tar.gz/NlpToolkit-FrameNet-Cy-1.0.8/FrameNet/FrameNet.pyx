import xml.etree.ElementTree

import pkg_resources

cdef class FrameNet:

    def __init__(self):
        self.__frames = []
        root = xml.etree.ElementTree.parse(pkg_resources.resource_filename(__name__, 'data/framenet.xml')).getroot()
        for frame_node in root:
            frame = Frame(frame_node.attrib["NAME"])
            for child_node in frame_node:
                if child_node.tag == "LEXICAL_UNITS":
                    for lexical_unit in child_node:
                        frame.addLexicalUnit(lexical_unit.text)
                elif child_node.tag == "FRAME_ELEMENTS":
                    for frame_element in child_node:
                        frame.addFrameElement(frame_element.text)
            self.__frames.append(frame)

    cpdef bint lexicalUnitExists(self, str synSetId):
        cdef Frame frame
        for frame in self.__frames:
            if frame.lexicalUnitExists(synSetId):
                return True
        return False

    cpdef list getFrames(self, str synSetId):
        cdef list result
        cdef Frame frame
        result = []
        for frame in self.__frames:
            if frame.lexicalUnitExists(synSetId):
                result.append(frame)
        return result

    cpdef int size(self):
        return len(self.__frames)

    cpdef Frame getFrame(self, int index):
        return self.__frames[index]

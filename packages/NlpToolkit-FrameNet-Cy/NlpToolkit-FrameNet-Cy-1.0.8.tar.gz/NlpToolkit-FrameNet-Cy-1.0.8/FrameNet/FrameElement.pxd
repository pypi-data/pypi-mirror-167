cdef class FrameElement(object):

    cdef str __frame_element_type
    cdef str __frame
    cdef str __id

    cpdef initWithId(self, str frameElementType, str frame, str _id)
    cpdef str getFrameElementType(self)
    cpdef str getFrame(self)
    cpdef str getId(self)

from Sampling.CrossValidation cimport CrossValidation

cdef class KFoldCrossValidation(CrossValidation):

    cdef list __instance_list
    cdef int __N

    cpdef list getTrainFold(self, int k)
    cpdef list getTestFold(self, int k)
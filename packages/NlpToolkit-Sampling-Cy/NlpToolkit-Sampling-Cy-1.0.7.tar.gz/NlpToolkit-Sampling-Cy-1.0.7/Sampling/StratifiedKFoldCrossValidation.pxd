from Sampling.KFoldCrossValidation cimport KFoldCrossValidation


cdef class StratifiedKFoldCrossValidation(KFoldCrossValidation):

    cdef list __instance_lists
    cdef list _N

    cpdef list getTrainFold(self, int k)
    cpdef list getTestFold(self, int k)

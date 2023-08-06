import random


cdef class StratifiedKFoldCrossValidation(KFoldCrossValidation):

    def __init__(self,
                 instance_lists: list,
                 K: int,
                 seed: int):
        """
        A constructor of StratifiedKFoldCrossValidation class which takes as set of class samples as an array of array of
        instances, a K (K in K-fold cross-validation) and a seed number, then shuffles each class sample using the
        seed number.

        PARAMETERS
        ----------
        instance_lists : list
            Original class samples. Each element of the this array is a sample only from one class.
        K : int
            K in K-fold cross-validation
        seed : int
            Random number to create K-fold sample(s)
        """
        cdef int i
        self.__instance_lists = instance_lists
        self._N = []
        for i in range(len(instance_lists)):
            random.seed(seed)
            random.shuffle(instance_lists[i])
            self._N.append(len(instance_lists[i]))
        self.K = K

    cpdef list getTrainFold(self, int k):
        """
        getTrainFold returns the k'th train fold in K-fold stratified cross-validation.

        PARAMETERS
        ----------
        k : int
            index for the k'th train fold of the K-fold stratified cross-validation

        RETURNS
        -------
        list
            Produced training sample
        """
        cdef int i, j
        cdef list train_fold = []
        for i in range(len(self._N)):
            for j in range((k * self._N[i]) // self.K):
                train_fold.append(self.__instance_lists[i][j])
            for j in range(((k + 1) * self._N[i]) // self.K, self._N[i]):
                train_fold.append(self.__instance_lists[i][j])
        return train_fold

    cpdef list getTestFold(self, int k):
        """
        getTestFold returns the k'th test fold in K-fold stratified cross-validation.

        PARAMETERS
        ----------
        k : int
            index for the k'th test fold of the K-fold stratified cross-validation

        RETURNS
        -------
        list
            Produced testing sample
        """
        cdef int i, j
        cdef list test_fold = []
        for i in range(len(self._N)):
            for j in range((k * self._N[i]) // self.K, ((k + 1) * self._N[i]) // self.K):
                test_fold.append(self.__instance_lists[i][j])
        return test_fold

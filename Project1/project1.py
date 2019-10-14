"""
Greg Dews
CS390S
Project 1

testing---
        input - Me = Bi
        P'Bi = wt_B (single vector with eigenvector quantities)
        compare wt_B to each column of wt_A , if matching, it is that person
    
    adding efficiency to training
        shortcutting 2500 x 2500 array problem
        find eigenvector of A'A = P2 (40x40)
            rather than A*A' (2500x2500)
            A'*A * P2 = lamdaP2
            A A' A P2 = lamda A P2
            AA' Q = lamda Q 
            AA' P = lamda P
            ... therefore A P2 = P, or A (A'A)
    CMC curve - hint code in slides/codes posted
        rank 1 to 10

    Python coding notes
    numpy.transpose(matrix) to transpose
    reshape is numpy method
    Check faceRecoganition4faces.pdf for example of report?
    will discuss more by next time. Recommend download sample code and try
    """

    import cv2
    import numpy
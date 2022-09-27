program ejemp02 

  use,intrinsic :: ISO_Fortran_env

  INTEGER N , counte
  REAL point(3),x,y
  REAL pi
  pi=3.1415926
  
  N=10**7
  counte=0
  
  CALL init_random_seed()
  do i=1,N

     call random_number(point)
     point(1)=point(1)*pi
     point(2)=point(2)*2*pi



    x=point(3)*sin(point(1))*cos(point(2))
    y=point(3)*sin(point(1))*sin(point(2))

    
     if ( 0.25>=((x-0.5)**2 +y**2 ) ) then
       counte=counte+1 
     endif
    
end do

WRITE(*,*)  REAL(counte)/REAL(N)*(4/3*pi)


end program ejemp02


SUBROUTINE init_random_seed()
  INTEGER :: I,n,clock
  INTEGER, DIMENSION(:),ALLOCATABLE:: seed

  CALL RANDOM_SEED(size=n)
  ALLOCATE(seed(n))

  CALL SYSTEM_CLOCK(COUNT=clock)

  seed= clock*37*(/(i-1,i=1,n)/)
  CALL RANDOM_SEED(PUT=seed)

end SUBROUTINE

      program grid
c
c---- Writes a 3d grid of ghost atoms for C9H9+, C2
c---- The C2 axis coincides with the z axis, so we calculate y.ge.0,
c---- i.e. about 1/2 of the required points, the rest will need to be
c---- generated through symmetry operations,
c---- (x,y,z) -> (-x,-y,z)
c
      implicit real*8 (a-h, o-z)
      character*200 runfp, runf
      character*6 fileno
      logical fexist, fopen
      parameter (xmin = -3.5d0, xmax = 3.5d0,
     .           ymin = 0d0,    ymax = 4.5d0,
     .           zmin = -3d0,   zmax = 4d0, delta=0.25d0)
c
      n = 0
      m = 0
      nf = 0
      runfp = 'run'
c
      x = xmin
      do while (x.le.xmax)
        y = ymin
        do while (y.le.ymax)
          z = zmin
          do while (z.le.zmax)
            n = n + 1
            m = m + 1
            if ((n.eq.1).or.(m.gt.95)) then
              if (n.gt.1) then
                write (1, *)
                write (1, '(''!'')')
                close(1)
                fopen = .false.
                m = 1
              endif
              nf = nf + 1
              if (nf.gt.999999) then
                write (6, '(''Cannot handle more than 999999 files.'')')
                go to 100
              endif
              write (fileno, '(i6.6)') nf
              runf = fileno // '.' // trim(runfp)
              write (6, *) trim(runf)
              inquire (file = runf, exist = fexist)
              if (fexist) then
                open(1, file = runf, status = 'old')
                close(1, status = 'delete')
              endif
              open (1, file = runf, status = 'new')
              fopen = .true.
              write (1, '(''%NProc=4'')')
              write (1, '(''%Mem=4Gb'')')
              write (1, '(''# HF/6-311++G(d,p) SCF(Tight) '',
     .          ''NMR CPHF(Separate) Test'')')
              write (1, *)
              write (1, '(''C9H9+ HF/6-311++G(d,p) nmr '',
     .          ''partial 3d grid'')')
              write (1, *)
              write (1, '(''+1 1'')')
c
      write (1, '(''C,0,0.,0.,1.645014194'')')
      write (1, '(''C,0,0.4905022324,1.2427684773,1.1554414148'')')
      write (1, '(''C,0,-0.4905022324,-1.2427684773,1.1554414148'')')
      write (1, '(''C,0,0.0100585215,2.0928052569,0.1040785875'')')
      write (1, '(''C,0,-0.0100585215,-2.0928052569,0.1040785875'')')
      write (1, '(''C,0,-0.8152087457,1.6410894083,-0.9354914584'')')
      write (1, '(''C,0,0.8152087457,-1.6410894083,-0.9354914584'')')
      write (1, '(''C,0,-0.6569284614,0.2832859329,-1.251946014'')')
      write (1, '(''C,0,0.6569284614,-0.2832859329,-1.251946014'')')
      write (1, '(''H,0,0.,0.,2.7459418542'')')
      write (1, '(''H,0,1.0699783805,1.7858874614,1.9137457041'')')
      write (1, '(''H,0,-1.0699783805,-1.7858874614,1.9137457041'')')
      write (1, '(''H,0,0.12964425,3.1677255378,0.2859658405'')')
      write (1, '(''H,0,-0.12964425,-3.1677255378,0.2859658405'')')
      write (1, '(''H,0,-1.5936377795,2.2790433661,-1.3665504299'')')
      write (1, '(''H,0,1.5936377795,-2.2790433661,-1.3665504299'')')
      write (1, '(''H,0,-1.490812806,-0.3325910524,-1.6109751404'')')
      write (1, '(''H,0,1.490812806,0.3325910524,-1.6109751404'')')
c
            endif
            write (1, '(''Bq 0  '', 3F10.6)') x, y, z
            z = z + delta
          end do
          y = y + delta
        end do
        x = x + delta
      end do
 100  write (6, '(''Number of ghost atoms: '', I10)') n
      if (fopen) then
        write (1, *)
        write (1, '(''!'')')
        close(1)
      endif
c
      stop
      end

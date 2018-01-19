function [Er,C,Int] = vaporPhase(cg_0, Tr_min, Er_0, Er_max, nablaTr, de)


  # Parameters
  # cg_0: interface density
  # Tr_min: bottom temperature
  # Er_0: interface position
  # Er_max: column height
  # nablaTr: Temperature gradient
  # de: reduced gravitational energy spacing
  
  
  # Initial conditions
  nn = floor( (Er_max - Er_0) / de ) + 2;
  de_up = (Er_max - Er_0) / (nn-1);
  C = zeros(nn,1);
  Er = zeros(nn,1);
  Int = 0;

  C(1) = cg_0;
  Er(1) = Er_0;

  
  # Integrate differential equation
  
  for i = 2 : nn
    
    Er(i) = Er(i-1) + de_up;    
    
    Tr = Tr_min + nablaTr * Er(i);

    a = Tr / ((1.0 - C(i-1)/3.0)^2);

    b = 9.0 * C(i-1) / 4.0;
    
    f = (  C(i-1) + nablaTr*( C(i-1)/(1.0-C(i-1)/3.0) )  ) / ( a - b );
    
    C(i) = C(i-1) - de_up * f;
    
  endfor



  # Integrate density profile

  for i = 2 : nn

    Int = Int + 0.5 * (C(i) + C(i-1)) * de;
    
  endfor

  
endfunction
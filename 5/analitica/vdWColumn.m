###############################################################################################

# This script computes density profiles in a vdw column with fixed reduced temperature gradient

###############################################################################################

clear all;
clc;


# Reduced temperature
Tr_top = 0.99;
# Tr_bottom = 0.99;

# Reduced gravitational energy
Er_max = 1e-04;

# # Fixed temperature gradient
# nablaTr = (Tr_top - Tr_bottom) / Er_max;

# Integration parameters
de = Er_max / 5000;


# Reduced temperature initial conditions (Tr cl cg)
initialTr = [0.99 1.1 0.8 ;
	     0.95 1.3 0.5 ;
	     0.90 1.5 0.3 ;
	     0.70 1.9 0.1 ;
	     0.60 2.2 0.05 ;
	     0.50 2.4 0.025 ;
	     0.45 2.5 0.0125 ;
	     0.40 2.7 1.5625e-03];



# Average reduced concentration
c_bar = 1.00;

# Plot and write flags
plot_profile = false;
write_profile = true;
write_vfrac = false;




# Move over temperature

# TB = [0.99 0.95 0.9 0.8 0.7 0.6 0.5];
TB = [0.99];

for idx = 1 : size(TB,2)
# for Tr_bottom = 0.99 : 0.01 : 0.99

  Tr_bottom = TB(idx);
  
  # Initial interfacial position and temperature
  Tr      = (Tr_top + Tr_bottom) / 2;
  nablaTr = (Tr_top - Tr_bottom) / Er_max;  
  Er_int  = Er_max / 2.0;
  ETop    = Er_max;
  EBottom = 0;

  
  
  # Iteration over position

  while( abs(ETop - EBottom) > 1.0e-10 )

    # Equilibrium densities. Use linear interpolation to determine initial densities
    init_cl = interp1( initialTr(:,1), initialTr(:,2), Tr );
    init_cg = interp1( initialTr(:,1), initialTr(:,3), Tr );
    [c,fval,info] = fsolve(@(x) redConFunction(x,Tr), [init_cl;init_cg], optimset("TolX", 1e-10, "TolFun", 1e-10));


 
    # Compute vapor phase
    [Er_g,Cg,IntCg] = vaporPhase(c(2),Tr_bottom,Er_int, Er_max, nablaTr, de);
  
    
    # Compute liquid phase
    [Er_f,Cf,IntCf] = liquidPhase(c(1),Tr_bottom,Er_int, nablaTr, de);


    # Check mass conservation. Compute mass excess
    Mass = IntCg + IntCf  -  c_bar * Er_max;


    if( Mass >= 0 )

      # Too much liquid

      # Update interface position
      ETop = Er_int;
      Er_int = (Er_int + EBottom) / 2;    

    else

      # Too much gas

      # Update interface position
      EBottom = Er_int;
      Er_int  = (ETop + Er_int) / 2;

    endif


  endwhile

  
  # Keep data in Result
  Result(end+1,1) = Tr_top;
  Result(end,2) = Er_g(1) / Er_max;



  # Write profile
  if(write_profile == true)
  
    fname = sprintf("Er_%.5f_cbar_%.3f.dat",Er_max,c_bar);
    
    file = fopen(fname,"w");

    for i = 1 : size(Er_f,1)

      fprintf(file,"%e %e\n",Er_f(i),Cf(i));

    endfor

    for i = 1 : size(Er_g,1)

      fprintf(file,"%e %e\n",Er_g(i),Cg(i));

    endfor
    
    fclose(file);

  endif
    


  
endfor



if(write_vfrac == true)
  
  fname = sprintf("cbar_%.3f.dat",c_bar);
  file = fopen(fname,"w");
  for i = 1 : size(Result,1)
    fprintf(file,"%f %f \n",Result(i,1),Result(i,2));
  endfor
  fclose(file);

endif
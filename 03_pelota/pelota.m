clear all

n=10000000;
x0=0.9;
y0=0.2;
thet=0;
v=2.0;

dt=0.0001;

for(i=1:n)
  vx=v*cos(thet);
  vy=v*sin(thet);
    
  x=vx*dt+x0;
  y=vy*dt+y0;
    
  if (x>1)
    thet=pi -thet;
  elseif(y<0)
    thet=-thet;
  elseif (x<y)
    thet=pi*0.5-thet;
  end

  x0=x; 
  y0=y;


end

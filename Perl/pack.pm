package pack; 
  
# Defining sub-routine for Addition 
sub areaRectangle
{ 
    # Initializing Variables a & b 
    $a = $_[0]; 
    $b = $_[1]; 
      
    $a = $a * $b; 
      
    print "\n***Area is $a"; 
} 
  

1;
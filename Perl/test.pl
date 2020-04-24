
#seraching
$a = "GEEKSFORGEEKS"; 

if ($a =~ m[GEEKS])  
{ 
    print "Match Found\n"; 
} 

else 
{ 
    print "Match Not Found\n"; 
} 

# substitute operator

$str ="hello there";

$str =~ s/re/00/;

print "$str\n";

# group matching

$date = '03/26/1999';
$date =~ s#(\d+)/(\d+)/(\d+)#$3/$1/$2#;

print "$date\n";
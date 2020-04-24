
# file handling

my $filename = 'testFile.txt';
open(my $fh, '>', $filename) ;
print $fh "A B C";
close $fh;

# reading
my $filename = 'testFile.txt';
open(my $fh, '<', $filename) ;
print <$fh>;
close $fh;

print "\n reading done\n";

# regular expression

#seraching
$a = "GEEKSFORGEEKS"; 

if ($a =~ m[GEEKS])  
{ 
    print "\nMatch Found\n"; 
} 

else 
{ 
    print "\nMatch Not Found\n"; 
} 

# substitute operator

$str ="hello there";

$str =~ s/re/00/;

print "$str\n";

# group matching

$date = '03/26/1999';
$date =~ s#(\d+)/(\d+)/(\d+)#$3/$1/$2#;

print "$date\n";


 
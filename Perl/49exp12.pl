use 5.010;
use strict;
use warnings;


# input
say"enter your name :";
my $name = <STDIN>;
say"welcome $name ";


# datatypes
# scalar --> single value

my $Name = "mark";
my $age =30;
my $n1 =7;
my $n2 = $age +$n1;
say " $Name , $age  ,$n2";

# array
my @num =(282,329,9292);
say"$num[0]";
print" array :@num\n";

push @num,38;
print"@num\n";
pop @num;
print"@num\n";

#hash

my %mobileinfo =(
"ram"=>4,
"name"=>"oppo",
);

say "ram : $mobileinfo{'ram'}";

# loops

my @a = (1..9);
for my $i (@a){
	print("$i","\n");
}

# conditional statement

say"enter the number :";
my $num =<>;

if($num < 0 )
{
	say"negative";
}
elsif ($num ==0)
{
	say"zero";
}
else 
{
	say"positive";
}


# function

sub area
{
	my $side = $_[0];
	return ($side *$side);
} 

my $val = area(3);
say "$val";


# package collection of modules

use pack; 
  
print "Enter two sides :"; 

$a = <>; 
$b = <>; 
  

pack::areaRectangle($a, $b); 
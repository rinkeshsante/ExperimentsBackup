use strict;
use warnings;


package animal;
sub new
{
	my$class = shift;
	my$self ={
		'name'=>shift,
	};
	bless $self,$class;
	return $self;

}

sub func
{
	my $self =shift;
	return $self->{'name'}
}


1;
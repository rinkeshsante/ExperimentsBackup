use MIME::Lite;

$to = 'rinkesh.sante@somaiya.edu';
$cc = '';
$from = 'rinkesh.sante@somaiya.edu';
$subject = 'Test Email';
$message = 'test email for exp 15';

$msg = MIME::Lite->new(
                 From     => $from,
                 To       => $to,
                 Cc       => $cc,
                 Subject  => $subject,
                 Data     => $message
                 );
                     

$msg->send('smtp', "smtp.gmail.com", AuthUser=>'rinkesh.sante@somaiya.edu', AuthPass=>"");
print "Email Sent Successfully\n";



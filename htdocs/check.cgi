#!/usr/bin/perl -Tw

use strict;
use CGI;
#use Data::Dumper;

my($cgi) = new CGI;

print $cgi->header('text/html');
print $cgi->start_html(-title => "Example CGI script",
                       -BGCOLOR => 'red');
print $cgi->h1("CGI Example");
print $cgi->p, "This is an example of CGI\n";
print $cgi->p, "Parameters given to this script:\n";
print "<UL>\n";
foreach my $param ($cgi->param)
{
 print "<LI>", "$param ", $cgi->param($param), "\n";
}
print "</UL>";

#获取环境变量
#print Dumper(/%ENV);
print "path is $ENV{path}\n"; 

print $cgi->end_html, "\n";

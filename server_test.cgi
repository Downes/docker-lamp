#!/usr/bin/perl

#    gRSShopper 0.7  Server Test  0.2  -- gRSShopper server test module
#    26 April 2017 - Stephen Downes


#    Copyright (C) <2008>  <Stephen Downes, National Research Council Canada>

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

##########################################################################
# Servertest.pl
##########################################################################
	use CGI::Carp qw(fatalsToBrowser);
# ---------------------------------
# Let's see what our environment is
if (!$ENV{'SERVER_SOFTWARE'}) {
  $newline = "\n";
}
else {
  print "Content-type: text/html\n\n";
  $newline = "<br>";
 }
print "gRSShopper web server environment test.".$newline.$newline;

# --------------------------------------
# Check for the required version of PERL
eval "require 5.004";
print "Checking PERL version...";
if ($@) {
  print "$newline"."This program requires at least PERL version 5.004 or greater.$newline";
  exit;
} else {
print " <span style='color:green;'> OK</span>$newline";
}

# use local::lib; # sets up a local lib at ~/perl5

# -----------------------------------------------------
# Check that all of the required modules can be located



$|++;
my $missing = 0;
my @lissing_list;
my @modules = qw(CGI CGI::Carp CGI::Session File::Basename File::stat File::Find DBI LWP LWP::UserAgent
LWP::Simple MIME::Types MIME::Lite::TT::HTML HTML::Entities Scalar::Util Text::ParseWords Lingua::EN::Inflect
Net::Twitter::Lite::WithAPIv1_1 Image::Resize DateTime DateTime::TimeZone Time::Local Digest::SHA1
XML::OPML REST::Client JSON JSON::Parse JSON::XS URI::Escape Email::Stuffer Email::Sender::Transport::SMTP
Mastodon::Client);


foreach my $module (@modules) {
  print "Checking for $module. ";
  eval "use $module";
  if ($@) {
    print "<span style='color:red;'>The $module module could not be located.</span>$newline";
    $missing=1;
    push @missing_list,$module;
  } else {
    print "<span style='color:green;'> OK</span>$newline";
  }
}



# -------------
# Provide CPAN help

if ($missing eq "1") {



	print qq|$newline You are missing the following required Perl modules.<ul>|;
  foreach my $module (@missing_list) { print qq|<li>$module</li>|; }

  print qq|</ul>		$newline$newline
		<b>Getting Perl Modules</b>$newline <ul>
    <li>If you use cPanel there may be a 'Perl Modules' option that installs
modules for you. Type the name of the module listed here into the form and ask cPanel to install it.
   See <a href="https://www.interserver.net/tips/kb/install-perl-module-cpanel/">
https://www.interserver.net/tips/kb/install-perl-module-cpanel/</a>"</li>
    <li>Use the SSH command to access your server in a terminal window, then
use the cpan command to load it. The syntax is: <tt> cpan -i &lt;module name&gt; </tt> </li>
    <li>Download the module and install it manually.</li>
    </ul>
		For more information, please see:$newline
		<a href="http://www.cpan.org/modules/INSTALL.html">http://www.cpan.org/modules/INSTALL.html</a> $newline
		<a href="http://www.rcbowen.com/imho/perl/modules.html">http://www.rcbowen.com/imho/perl/modules.html</a> $newline|;

}

# -------------
# Test database access (from default config in Dockerfile)

print "<p>Testing database access (from default config in Dockerfile)</p>";
use DBI;

    	# Make variables easy to read :)
    	my $dbname = "grsshopper";
    	my $dbhost = "localhost";
    	my $usr = "grsshopper_user";
    	my $pwd = "user_password";

	# Connect to the Database
  	my $dbh = DBI->connect("DBI:mysql:database=$dbname;host=$dbhost;port=3306",$usr,$pwd);

	# Catch connection error
	if( ! $dbh ) {

              print "Content-type: text/html\n\n";
	      print "Database connection error for db '$dbname'. Please contact the site administrator.<br>";   

		# Print error report and exit
		print "Error String Reported: $DBI::errstr <br>";
		exit;

	# I'll put more error-checking here
	} else {
	
	        print "<p>Database successfully connected.</p>";
		eval {
		#$dbh->do( whatever );
		#$dbh->{dbh}->do( something else );
		};

		if( $@ ) {
			print "Ugg, problem: $@\n";
		}
	}



exit;
